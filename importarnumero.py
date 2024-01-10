from telethon.sync import TelegramClient
import pickle
import os

def add_session_to_vars(session_file, vars_file, api_id, api_hash):
    try:
        client = TelegramClient(session_file, api_id, api_hash)
        client.start()
        phone_number = client.get_me().phone
        client.disconnect()

        with open(vars_file, 'ab') as f:
            pickle.dump([phone_number], f)
            print(f'[*] Added {phone_number} to {vars_file}')
    except Exception as e:
        print(f'[!] Error adding session: {str(e)}')

def main():
    api_id = 16746680  # Substitua pelo seu ID de API
    api_hash = 'd038e172eb99839b69c39c3c25cd98cf'  # Substitua pelo seu hash de API
    vars_file = 'vars.txt'

    sessions_folder = os.path.dirname(os.path.abspath(__file__))  # Pasta do script

    if not os.path.exists(vars_file):
        print(f'[!] O arquivo {vars_file} não existe. Criando o arquivo...')
        with open(vars_file, 'wb'):  # Cria o arquivo vars.txt se não existir
            pass

    for session_file in os.listdir(sessions_folder):
        if session_file.endswith('.session'):
            add_session_to_vars(os.path.join(sessions_folder, session_file), vars_file, api_id, api_hash)

    print('[*] Sessões importadas com sucesso!')
    input('Pressione Enter para sair...')

if __name__ == "__main__":
    main()
