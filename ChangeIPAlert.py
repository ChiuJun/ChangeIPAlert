import io,json,os
import public_ip as ip
import urllib.parse
import urllib.request

class ChangeIPAlert():

    def __init__(self):
        self.load_parameters()

        new_ip = ip.get()
        if new_ip:
            if not new_ip == self._old_ip:
                print("The IP change from {} to {}".format(self._old_ip,new_ip))
                self.send_alert(new_ip)


    def load_parameters(self):
        __location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
        self.config_file = __location__+'/config.json'
        if(os.path.exists(self.config_file)):
            with open(self.config_file) as f:
                self.parameters = json.load(f)

                self._old_ip = self.parameters["IP"]
                self._api_key = self.parameters["SendKey"]
                self._old_resp = self.parameters["Response"]
            
            f.close()
        else:
            print("config.json does not exist")
            exit()


    def update_parameters(self,ip,result):
        self.parameters["IP"] = ip
        self.parameters["Response"] = result
        with open(self.config_file, "w") as jsonFile:
            json.dump(self.parameters, jsonFile)
        jsonFile.close()

    def sc_send(self,text, desp='', key='[SENDKEY]'):
        postdata = urllib.parse.urlencode({'text': text, 'desp': desp}).encode('utf-8')
        url = f'https://sctapi.ftqq.com/{key}.send'
        req = urllib.request.Request(url, data=postdata, method='POST')
        with urllib.request.urlopen(req) as response:
            result = response.read().decode('utf-8')
        return result


    def send_alert(self,ip):
        desp = 'New IPv4 address: {}'.format(ip)
        result = self.sc_send('IP Changes', desp, self._api_key)
        self.update_parameters(ip,result)
        

if __name__ == "__main__":
    alertas = ChangeIPAlert()