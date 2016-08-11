import sys
import hashlib
#import os #only for unix


def main(argv):
    if len(argv) != 1:
        sys.exit('Utilizacao: storepass.py <file_name>')

    print('\nArmazenamento de Usuario e Senha\n')

    if input('O arquivo ' + sys.argv[
        1] + ' sera sobrescrito.\nContinuar (S/n): ') not in ('S', 's'):
        sys.exit('\nAlteracoes nao realizadas.\n')

    usern = input('Nome do usuario: ')
    #os.system("stty -echo") #only for unix
    passwd = input('Senha: ')
    #os.system("stty echo") #only for unix
    passwd = hashlib.sha224(passwd.encode('utf-8')).hexdigest()

    try:
        file_conn = open(sys.argv[1], 'a')
        file_conn.write(usern + ':' + passwd + '\n')
        file_conn.close()
    except:
        sys.exit('Falha ao escrever o arquivo!')

    print('\nSenha registrada ' + sys.argv[1] + '\n')


if __name__ == "__main__":
    main(sys.argv[1:])