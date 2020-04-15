import time
import requests
from bs4 import BeautifulSoup
from plyer import notification
def activate_notification(title,message,timeout):
    notification.notify(title=title,message=message,timeout=timeout)
def getwhodata(url):
    try:
        req=requests.get(url).text
    except:
        activate_notification("D33P C0D3","Internet connection is not Responding",4)
        exit(1)
    soup = BeautifulSoup(req, 'html.parser')
    myDataStr=""
    for tr in soup.find_all('tbody')[0].find_all('tr'):
        myDataStr += tr.get_text()
    itemList = myDataStr.split("\n\n")
    statedata=[]
    for i in itemList:
        statedata.append(list(i.strip("\n").strip("").split("\n")))
    return statedata
if __name__=="__main__":
    activate_notification("D33P C0D3","Corona Update Assistant is ACTIVATED \nSTAY HOME ! STAY SAFE !",3)
    while True:
        rawdata=getwhodata('https://www.mohfw.gov.in/')
        sdata=rawdata[:-4];totalcase=rawdata[-4][1];totaldeath=[-2];totalcured=[-3]
        counter=1
        datalist=f"{sdata[0][1]}\tC: {sdata[0][2]} D: {sdata[0][3]}"
        for i in sdata:
            if (counter%4)==0:
                activate_notification()
            state=i[1];case=i[2];Cured=i[3];death=i[4]
            title=f"D33p C0D3----- COVID-19 Cases In India: {totalcase}"
            Head=f"\n{state} State Report\n\n"
            ndataE=f"Cases: {case} -- Cured: {Cured} -- Death: {death}"
            ndataH=f"संपूर्ण: {case} -- ठीक हुए: {Cured} -- मृतक: {death}"
            activate_notification(title,Head+ndataE+"\n"+ndataH,5)
            try:
                time.sleep(5)
            except:
                exit(0)
