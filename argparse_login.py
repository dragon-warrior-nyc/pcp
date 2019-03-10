import argparse

def check_arg():
    parser = argparse.ArgumentParser(description='Script to login')

    parser.add_argument('-H', '--host',
                        help='host ip',
                        required='True')

    parser.add_argument('-p', '--port',
                        help='port of the web server',
                        default='8080')

    parser.add_argument('-u', '--user',
                        help='user name',
                        default='root')

    results = parser.parse_args()

    return (results.host,
            results.port,
            results.user)

if __name__ == '__main__':
    h, p, u = check_arg()
    print(f'h = {h}')
    print(f'p = {p}')
    print(f'u = {u}')

# try the following in command line:
# python argparse_login.py -H 192.17.23.5 -p 9200 -u mat
# python argparse_login.py -H 192.17.23.5 -p 9200
# python argparse_login.py -H 192.17.23.5
# python argparse_login.py
# python argparse_login.py -h
