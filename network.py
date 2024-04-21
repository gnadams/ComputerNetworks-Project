import speedtest   



def get_network_speed():
    st = speedtest.Speedtest() 
    error = False
    down_speed=0
    up_speed=0
    ping = 0
    try:
        
        down_speed = st.download()
        up_speed = st.upload()
        ping = st.results.ping
        
    except:
        error = True

    return {"error": error,"upload" : up_speed, "download": down_speed, "ping":ping}

if __name__ == "__main__":
    test = get_network_speed()


    
