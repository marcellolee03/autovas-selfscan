import time
from getpass import getpass
from datetime import datetime
from core import ask_LLM, check_pass, init_scan, manage_scan

API_KEY = ''
API_URL = ''

password = getpass('Input user password: ')
openvas_username = input('Input OpenVAS username: ')
openvas_password = getpass('Input OpenVAS password: ')

if check_pass.check_sudo_pass(password):

    # Creating and starting scan
    taskname = datetime.now().strftime("self_scan_%d-%m-%y_%H-%M")

    print('Creating target...')
    init_scan.create_target(password, openvas_username, openvas_password)

    print('Creating task...')
    init_scan.create_task(password, openvas_username, openvas_password, taskname)

    print('Starting scan...')
    init_scan.start_scan(password, openvas_username, openvas_password, taskname)


    # Waiting for scan to finish
    while not manage_scan.check_progress(password, openvas_username, openvas_password, taskname):
        time.sleep(5)


    # Saving report as csv
    report_id = manage_scan.get_report(password, openvas_username, openvas_password, taskname)['id']
    manage_scan.save_report(report_id, password, openvas_username, openvas_password, taskname)


    # Starting timer
    start = time.time()


    # Generating shell script w/ GEMINI-2.0-FLASH
    headers = ['CVEs','NVT Name','Port','Port Protocol','Summary', 'Specific Result', 'Vulnerability Detection Method','Affected Software/OS','Solution']

    prompt = ask_LLM.generate_prompt(f'reports/{taskname}.csv', 0, headers)
    response = ask_LLM.ask_gemini(API_KEY, prompt)


    # Saving script
    caminho = f'generatedscripts/{taskname}.sh'
    with open(caminho, 'w') as file:
        file.write(response)
        
    print(f'Script salvo em: {caminho}')

    # Ending timer
    finish = time.time()

    print(response)
    print(f'time elapsed: {((finish - start)/60):.2f} minutes')

else:
    print("Wrong password. Shutting down.")
