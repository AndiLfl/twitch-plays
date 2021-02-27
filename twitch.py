import socket
import sys
import re


class Twitch:
    username = ""
    oauth = ""
    chan = "#Channel"
    s = None

    @staticmethod
    def twitch_login_status(data):
        if not re.match(r'^:(testserver\.local|tmi\.twitch\.tv) NOTICE \* :Login unsuccessful\r\n$', data.decode('utf-8')):
            return True
        else:
            return False

    def twitch_connect(self, user, key):
        self.username = user
        self.oauth = key
        print("Connecting to twitch.tv")
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(0.6)
        connect_host = "irc.twitch.tv"
        connect_port = 6667
        try:
            s.connect((connect_host, connect_port))
        except:
            print("Failed to connect to twitch")
            sys.exit()
        print("Connected to twitch")
        print("Sending our details to twitch...")
        s.send(bytes('USER %s\r\n' % self.username, 'utf-8'))
        s.send(bytes('PASS %s\r\n' % self.oauth, 'utf-8'))
        s.send(bytes('NICK %s\r\n' % self.username, 'utf-8'))

        if not self.twitch_login_status(s.recv(1024)):
            print("... and they didn't accept our details")
            sys.exit()
        else:
            print("... they accepted our details")
            print("Connected to twitch.tv!")
            self.s = s
            s.send(bytes('JOIN #%s\r\n' % self.username, 'utf-8'))
            s.recv(1024)

    def check_has_message(self, data):
        return re.match(
            r'^:[a-zA-Z0-9_]+\![a-zA-Z0-9_]+@[a-zA-Z0-9_]+(\.tmi\.twitch\.tv|\.testserver\.local) PRIVMSG #[a-zA-Z0-9_]+ :.+$',
            data.decode('utf-8'))

    def parse_message(self, data):
        return {
            'channel': re.findall(r'^:.+\![a-zA-Z0-9_]+@[a-zA-Z0-9_]+.+ PRIVMSG (.*?) :', data)[0],
            'username': re.findall(r'^:([a-zA-Z0-9_]+)\!', data)[0],
            'message': re.findall(r'PRIVMSG #[a-zA-Z0-9_]+ :(.+)', data)[0]
        }

    def twitch_recieve_messages(self):
        data = None
        try:
            data = self.s.recv(1024)
        except:
            return False

        if not data:
            print("Lost connection to Twitch, attempting to reconnect...")
            self.twitch_connect(self.user, self.oauth)
            return None

        # self.ping(data)

        if self.check_has_message(data):
            return [self.parse_message(line) for line in filter(None, data.decode('utf-8').split('\r\n'))]
