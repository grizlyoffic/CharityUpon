import requests , os , psutil , sys , jwt , pickle , json , binascii , time , urllib3 , base64 , datetime , re , socket , threading , ssl , pytz , aiohttp , random
from flask import Flask, request, jsonify
from protobuf_decoder.protobuf_decoder import Parser
from xC4 import * ; from xHeaders import *
from datetime import datetime
from google.protobuf.timestamp_pb2 import Timestamp
from concurrent.futures import ThreadPoolExecutor
from threading import Thread
from Pb2 import DEcwHisPErMsG_pb2 , MajoRLoGinrEs_pb2 , PorTs_pb2 , MajoRLoGinrEq_pb2 , sQ_pb2 , Team_msg_pb2
from cfonts import render, say


#EMOTES BY NAJMI_FF_EXPERIMENT



urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)  

# VariabLes dyli 
#------------------------------------------#
online_writer = None
whisper_writer = None
spam_room = False
spammer_uid = None
spam_chat_id = None
spam_uid = None
Spy = False
Chat_Leave = False
#------------------------------------------#

app = Flask(__name__)

Hr = {
    'User-Agent': "Dalvik/2.1.0 (Linux; U; Android 11; ASUS_Z01QD Build/PI)",
    'Connection': "Keep-Alive",
    'Accept-Encoding': "gzip",
    'Content-Type': "application/x-www-form-urlencoded",
    'Expect': "100-continue",
    'X-Unity-Version': "2018.4.11f1",
    'X-GA': "v1 1",
    'ReleaseVersion': "OB52"}

# ---- MULTI-REGION ACCOUNTS CONFIGURATION ----
available_regions = ["ME", "IND", "VN", "TH", "BD", "PK", "TW", "EU", "NA", "SAC", "BR"]

# Har region mein 6 accounts (UID, Password) pairs
region_accounts = {
    "ME": [
        ("4512667980", "CZY-8UZBP5UXX-NEXU"),
        ("4512666865", "CZY-UGP2FSOH6-NEXU"),
        ("4512665744", "CZY-CSLIZXU2B-NEXU"),
        ("4512672537", "CZY-7UM00CC82-NEXU"),
        ("4512671613", "CZY-NVNOTXLZX-NEXU"),
        ("4512670501", "CZY-8LHBK1JGX-NEXU"),
    ],
    "IND": [
        ("4511865130", "CZY-JMJ0ZZQCO-NEXU"),
        ("4511865702", "CZY-VEDGBAZKU-NEXU"),
        ("4511865288", "CZY-QDBIIJTMX-NEXU"),
        ("4511865254", "CZY-GADO7Y12X-NEXU")
        ("4512655524", "CZY-ZMMSWMKZG-NEXU"),
        ("4512656681", "CZY-QQPEVEYMT-NEXU"),
    ],
    "VN": [
        ("4511868460", "CZY-REPOHY0ON-NEXU"),
        ("4511868299", "CZY-7GWK6HPI3-NEXU"),
        ("4511868315", "CZY-RMX9H94LR-NEXU"),
        ("4511868273", "CZY-VDNV5SZP4-NEXU"),
        ("4511868332", "CZY-YIHYYHSPO-NEXU"),
        ("4511867912", "CZY-VFANXWL7C-NEXU"),
    ],
    "TH": [
        ("4511868893", "CZY-CKP4TABXE-NEXU"),
        ("4511868888", "CZY-QXV017P6N-NEXU"),
        ("4511868892", "CZY-PCZBGO0BW-NEXU"),
        ("4511868905", "CZY-EWHQDTLYM-NEXU"),
        ("4511868907", "CZY-XZZNUZOZJ-NEXU"),
        ("4511868953", "CZY-OX2XNTYPY-NEXU"),
    ],
    "BD": [
        ("4511869400", "CZY-57JZMCJUB-NEXU"),
        ("4511869389", "CZY-5NSVZYUOV-NEXU"),
        ("4511869399", "CZY-ZM3D28C6R-NEXU"),
        ("4511869383", "CZY-9A29DYKQI-NEXU"),
        ("4512677536", "CZY-ZPFG5PXCV-NEXU"),
        ("4512677040", "CZY-YPVJ8PQPE-NEXU"),
    ],
    "PK": [
        ("4512633903", "CZY-HUFQQOMRC-NEXU"),
        ("4512639336", "CZY-1TNFQ5CDE-NEXU"),
        ("4512638604", "CZY-43C2KXVEQ-NEXU"),
        ("4512641428", "CZY-TQAPWSH5N-NEXU"),
        ("4512643792", "CZY-26FVQA14T-NEXU"),
        ("4512642778", "CZY-GUC0JNCCZ-NEXU"),
    ],
    "TW": [
        ("4511872207", "CZY-ZGJP8OEUM-NEXU"),
        ("4511872494", "CZY-HICKKASWA-NEXU"),
        ("4511872245", "CZY-NM9I1CICU-NEXU"),
        ("4511872497", "CZY-OFBB1JSCF-NEXU"),
        ("4511871767", "CZY-GI4AQWLOC-NEXU"),
        ("4511872283", "CZY-GWTNBHAYC-NEXU"),
    ],
    "EU": [
        ("4511873010", "CZY-AD3OLKSE6-NEXU"),
        ("4511873007", "CZY-LQSTOEBMX-NEXU"),
        ("4511872970", "CZY-0FIINQJTH-NEXU"),
        ("4511873062", "CZY-BBESVCJGN-NEXU"),
        ("4512680928", "CZY-BBNVHUX94-NEXU"),
        ("4512679713", "CZY-Q4YKTPQTS-NEXU"),
    ],
    "NA": [
        ("4511876283", "CZY-STLUP6YKP-NEXU"),
        ("4511876275", "CZY-CYWVVDQYD-NEXU"),
        ("4511876281", "CZY-KMQKOCWPM-NEXU"),
        ("4511875862", "CZY-QCEEAJNBF-NEXU"),
        ("4511876290", "CZY-LBDOISOVJ-NEXU"),
        ("4511876278", "CZY-GVMFAFRZE-NEXU"),
    ],
    "SAC": [
        ("4511876627", "CZY-K4WRVBOOU-NEXU"),
        ("4511876585", "CZY-9D43JADQR-NEXU"),
        ("4511876625", "CZY-FI3XW9IHL-NEXU"),
        ("4511876632", "CZY-OW2S1OYBW-NEXU"),
        ("4511876631", "CZY-IA29WMDSK-NEXU"),
        ("4511876586", "CZY-2M2PJ9VGP-NEXU"),
    ],
    "BR": [
        ("4511876973", "CZY-JBUNOTUWV-NEXU"),
        ("4511876927", "CZY-QKIDZZEDQ-NEXU"),
        ("4511876886", "CZY-M1WZHNNUA-NEXU"),
        ("4511876933", "CZY-CREAQRO1O-NEXU"),
        ("4511876881", "CZY-2RPSRODMU-NEXU"),
        ("4511877361", "CZY-TRBNEQUX7-NEXU"),
    ],
}


# Dictionary to store active bot instances per region
active_bots = {}
bot_instances_lock = threading.Lock()

# ---- Random Colores ----
def get_random_color():
    colors = [
        "[FF0000]", "[00FF00]", "[0000FF]", "[FFFF00]", "[FF00FF]", "[00FFFF]", "[FFFFFF]", "[FFA500]",
        "[A52A2A]", "[800080]", "[000000]", "[808080]", "[C0C0C0]", "[FFC0CB]", "[FFD700]", "[ADD8E6]",
        "[90EE90]", "[D2691E]", "[DC143C]", "[00CED1]", "[9400D3]", "[F08080]", "[20B2AA]", "[FF1493]",
        "[7CFC00]", "[B22222]", "[FF4500]", "[DAA520]", "[00BFFF]", "[00FF7F]", "[4682B4]", "[6495ED]",
        "[5F9EA0]", "[DDA0DD]", "[E6E6FA]", "[B0C4DE]", "[556B2F]", "[8FBC8F]", "[2E8B57]", "[3CB371]",
        "[6B8E23]", "[808000]", "[B8860B]", "[CD5C5C]", "[8B0000]", "[FF6347]", "[FF8C00]", "[BDB76B]",
        "[9932CC]", "[8A2BE2]", "[4B0082]", "[6A5ACD]", "[7B68EE]", "[4169E1]", "[1E90FF]", "[191970]",
        "[00008B]", "[000080]", "[008080]", "[008B8B]", "[B0E0E6]", "[AFEEEE]", "[E0FFFF]", "[F5F5DC]",
        "[FAEBD7]"
    ]
    return random.choice(colors)

async def encrypted_proto(encoded_hex):
    key = b'Yg&tc%DEuh6%Zc^8'
    iv = b'6oyZDr22E3ychjM%'
    cipher = AES.new(key, AES.MODE_CBC, iv)
    padded_message = pad(encoded_hex, AES.block_size)
    encrypted_payload = cipher.encrypt(padded_message)
    return encrypted_payload
    
async def GeNeRaTeAccEss(uid , password):
    url = "https://100067.connect.garena.com/oauth/guest/token/grant"
    headers = {
        "Host": "100067.connect.garena.com",
        "User-Agent": (await Ua()),
        "Content-Type": "application/x-www-form-urlencoded",
        "Accept-Encoding": "gzip, deflate, br",
        "Connection": "close"}
    data = {
        "uid": uid,
        "password": password,
        "response_type": "token",
        "client_type": "2",
        "client_secret": "2ee44819e9b4598845141067b281621874d0d5d7af9d8f7e00c1e54715b7d1e3",
        "client_id": "100067"}
    async with aiohttp.ClientSession() as session:
        async with session.post(url, headers=Hr, data=data) as response:
            if response.status != 200: return "Failed to get access token"
            data = await response.json()
            open_id = data.get("open_id")
            access_token = data.get("access_token")
            return (open_id, access_token) if open_id and access_token else (None, None)

async def EncRypTMajoRLoGin(open_id, access_token):
    major_login = MajoRLoGinrEq_pb2.MajorLogin()
    major_login.event_time = str(datetime.now())[:-7]
    major_login.game_name = "free fire"
    major_login.platform_id = 1
    major_login.client_version = "1.120.2"
    major_login.system_software = "Android OS 9 / API-28 (PQ3B.190801.10101846/G9650ZHU2ARC6)"
    major_login.system_hardware = "Handheld"
    major_login.telecom_operator = "Verizon"
    major_login.network_type = "WIFI"
    major_login.screen_width = 1920
    major_login.screen_height = 1080
    major_login.screen_dpi = "280"
    major_login.processor_details = "ARM64 FP ASIMD AES VMH | 2865 | 4"
    major_login.memory = 3003
    major_login.gpu_renderer = "Adreno (TM) 640"
    major_login.gpu_version = "OpenGL ES 3.1 v1.46"
    major_login.unique_device_id = "Google|34a7dcdf-a7d5-4cb6-8d7e-3b0e448a0c57"
    major_login.client_ip = "223.191.51.89"
    major_login.language = "en"
    major_login.open_id = open_id
    major_login.open_id_type = "4"
    major_login.device_type = "Handheld"
    memory_available = major_login.memory_available
    memory_available.version = 55
    memory_available.hidden_value = 81
    major_login.access_token = access_token
    major_login.platform_sdk_id = 1
    major_login.network_operator_a = "Verizon"
    major_login.network_type_a = "WIFI"
    major_login.client_using_version = "7428b253defc164018c604a1ebbfebdf"
    major_login.external_storage_total = 36235
    major_login.external_storage_available = 31335
    major_login.internal_storage_total = 2519
    major_login.internal_storage_available = 703
    major_login.game_disk_storage_available = 25010
    major_login.game_disk_storage_total = 26628
    major_login.external_sdcard_avail_storage = 32992
    major_login.external_sdcard_total_storage = 36235
    major_login.login_by = 3
    major_login.library_path = "/data/app/com.dts.freefireth-YPKM8jHEwAJlhpmhDhv5MQ==/lib/arm64"
    major_login.reg_avatar = 1
    major_login.library_token = "5b892aaabd688e571f688053118a162b|/data/app/com.dts.freefireth-YPKM8jHEwAJlhpmhDhv5MQ==/base.apk"
    major_login.channel_type = 3
    major_login.cpu_type = 2
    major_login.cpu_architecture = "64"
    major_login.client_version_code = "2019118695"
    major_login.graphics_api = "OpenGLES2"
    major_login.supported_astc_bitset = 16383
    major_login.login_open_id_type = 4
    major_login.analytics_detail = b"FwQVTgUPX1UaUllDDwcWCRBpWAUOUgsvA1snWlBaO1kFYg=="
    major_login.loading_time = 13564
    major_login.release_channel = "android"
    major_login.extra_info = "KqsHTymw5/5GB23YGniUYN2/q47GATrq7eFeRatf0NkwLKEMQ0PK5BKEk72dPflAxUlEBir6Vtey83XqF593qsl8hwY="
    major_login.android_engine_init_flag = 110009
    major_login.if_push = 1
    major_login.is_vpn = 1
    major_login.origin_platform_type = "4"
    major_login.primary_platform_type = "4"
    string = major_login.SerializeToString()
    return  await encrypted_proto(string)

async def MajorLogin(payload):
    url = "https://loginbp.ggblueshark.com/MajorLogin"
    ssl_context = ssl.create_default_context()
    ssl_context.check_hostname = False
    ssl_context.verify_mode = ssl.CERT_NONE
    async with aiohttp.ClientSession() as session:
        async with session.post(url, data=payload, headers=Hr, ssl=ssl_context) as response:
            if response.status == 200: return await response.read()
            return None

async def GetLoginData(base_url, payload, token):
    url = f"{base_url}/GetLoginData"
    ssl_context = ssl.create_default_context()
    ssl_context.check_hostname = False
    ssl_context.verify_mode = ssl.CERT_NONE
    Hr['Authorization']= f"Bearer {token}"
    async with aiohttp.ClientSession() as session:
        async with session.post(url, data=payload, headers=Hr, ssl=ssl_context) as response:
            if response.status == 200: return await response.read()
            return None

async def DecRypTMajoRLoGin(MajoRLoGinResPonsE):
    proto = MajoRLoGinrEs_pb2.MajorLoginRes()
    proto.ParseFromString(MajoRLoGinResPonsE)
    return proto

async def DecRypTLoGinDaTa(LoGinDaTa):
    proto = PorTs_pb2.GetLoginData()
    proto.ParseFromString(LoGinDaTa)
    return proto

async def DecodeWhisperMessage(hex_packet):
    packet = bytes.fromhex(hex_packet)
    proto = DEcwHisPErMsG_pb2.DecodeWhisper()
    proto.ParseFromString(packet)
    return proto
    
async def decode_team_packet(hex_packet):
    packet = bytes.fromhex(hex_packet)
    proto = sQ_pb2.recieved_chat()
    proto.ParseFromString(packet)
    return proto
    
async def xAuThSTarTuP(TarGeT, token, timestamp, key, iv):
    uid_hex = hex(TarGeT)[2:]
    uid_length = len(uid_hex)
    encrypted_timestamp = await DecodE_HeX(timestamp)
    encrypted_account_token = token.encode().hex()
    encrypted_packet = await EnC_PacKeT(encrypted_account_token, key, iv)
    encrypted_packet_length = hex(len(encrypted_packet) // 2)[2:]
    if uid_length == 9: headers = '0000000'
    elif uid_length == 8: headers = '00000000'
    elif uid_length == 10: headers = '000000'
    elif uid_length == 7: headers = '000000000'
    else: print('Unexpected length') ; headers = '0000000'
    return f"0115{headers}{uid_hex}{encrypted_timestamp}00000{encrypted_packet_length}{encrypted_packet}"
     
async def cHTypE(H):
    if not H: return 'Squid'
    elif H == 1: return 'CLan'
    elif H == 2: return 'PrivaTe'
    
async def SEndMsG(H , message , Uid , chat_id , key , iv):
    TypE = await cHTypE(H)
    if TypE == 'Squid': msg_packet = await xSEndMsgsQ(message , chat_id , key , iv)
    elif TypE == 'CLan': msg_packet = await xSEndMsg(message , 1 , chat_id , chat_id , key , iv)
    elif TypE == 'PrivaTe': msg_packet = await xSEndMsg(message , 2 , Uid , Uid , key , iv)
    return msg_packet

async def SEndPacKeT(OnLinE , ChaT , TypE , PacKeT):
    if TypE == 'ChaT' and ChaT: whisper_writer.write(PacKeT) ; await whisper_writer.drain()
    elif TypE == 'OnLine': online_writer.write(PacKeT) ; await online_writer.drain()
    else: return 'UnsoPorTed TypE ! >> ErrrroR (:():)' 
           
async def TcPOnLine(ip, port, key, iv, AutHToKen, reconnect_delay=0.5):
    global online_writer , spam_room , whisper_writer , spammer_uid , spam_chat_id , spam_uid , XX , uid , Spy,data2, Chat_Leave
    while True:
        try:
            reader , writer = await asyncio.open_connection(ip, int(port))
            online_writer = writer
            bytes_payload = bytes.fromhex(AutHToKen)
            online_writer.write(bytes_payload)
            await online_writer.drain()
            while True:
                data2 = await reader.read(9999)
                if not data2: break
                
                if data2.hex().startswith('0500') and len(data2.hex()) > 1000:
                    try:
                        print(data2.hex()[10:])
                        packet = await DeCode_PackEt(data2.hex()[10:])
                        print(packet)
                        packet = json.loads(packet)
                        OwNer_UiD , CHaT_CoDe , SQuAD_CoDe = await GeTSQDaTa(packet)

                        JoinCHaT = await AutH_Chat(3 , OwNer_UiD , CHaT_CoDe, key,iv)
                        await SEndPacKeT(whisper_writer , online_writer , 'ChaT' , JoinCHaT)


                        message = f'[B][C]{get_random_color()}\n- WeLComE To Emote Bot ! '
                        P = await SEndMsG(0 , message , OwNer_UiD , OwNer_UiD , key , iv)
                        await SEndPacKeT(whisper_writer , online_writer , 'ChaT' , P)

                    except:
                        if data2.hex().startswith('0500') and len(data2.hex()) > 1000:
                            try:
                                print(data2.hex()[10:])
                                packet = await DeCode_PackEt(data2.hex()[10:])
                                print(packet)
                                packet = json.loads(packet)
                                OwNer_UiD , CHaT_CoDe , SQuAD_CoDe = await GeTSQDaTa(packet)

                                JoinCHaT = await AutH_Chat(3 , OwNer_UiD , CHaT_CoDe, key,iv)
                                await SEndPacKeT(whisper_writer , online_writer , 'ChaT' , JoinCHaT)


                                message = f'[B][C]{get_random_color()}\n- WeLComE To Emote Bot ! \n\n{get_random_color()}- Commands : @a {xMsGFixinG("123456789")} {xMsGFixinG("909000001")}\n\n[00FF00]Dev : @{xMsGFixinG("DEVXTLIVE")}'
                                P = await SEndMsG(0 , message , OwNer_UiD , OwNer_UiD , key , iv)
                                await SEndPacKeT(whisper_writer , online_writer , 'ChaT' , P)
                            except:
                                pass

            online_writer.close() ; await online_writer.wait_closed() ; online_writer = None

        except Exception as e: print(f"- ErroR With {ip}:{port} - {e}") ; online_writer = None
        await asyncio.sleep(reconnect_delay)
                            
async def TcPChaT(ip, port, AutHToKen, key, iv, LoGinDaTaUncRypTinG, ready_event, region , reconnect_delay=0.5):
    print(region, 'TCP CHAT')

    global spam_room , whisper_writer , spammer_uid , spam_chat_id , spam_uid , online_writer , chat_id , XX , uid , Spy,data2, Chat_Leave
    while True:
        try:
            reader , writer = await asyncio.open_connection(ip, int(port))
            whisper_writer = writer
            bytes_payload = bytes.fromhex(AutHToKen)
            whisper_writer.write(bytes_payload)
            await whisper_writer.drain()
            ready_event.set()
            if LoGinDaTaUncRypTinG.Clan_ID:
                clan_id = LoGinDaTaUncRypTinG.Clan_ID
                clan_compiled_data = LoGinDaTaUncRypTinG.Clan_Compiled_Data
                print('\n - TarGeT BoT in CLan ! ')
                print(f' - Clan Uid > {clan_id}')
                print(f' - BoT ConnEcTed WiTh CLan ChaT SuccEssFuLy ! ')
                pK = await AuthClan(clan_id , clan_compiled_data , key , iv)
                if whisper_writer: whisper_writer.write(pK) ; await whisper_writer.drain()
            while True:
                data = await reader.read(9999)
                if not data: break
                
                if data.hex().startswith("120000"):

                    msg = await DeCode_PackEt(data.hex()[10:])
                    chatdata = json.loads(msg)
                    try:
                        response = await DecodeWhisperMessage(data.hex()[10:])
                        uid = response.Data.uid
                        chat_id = response.Data.Chat_ID
                        XX = response.Data.chat_type
                        inPuTMsG = response.Data.msg.lower()
                    except:
                        response = None


                    if response:
                        if inPuTMsG.startswith(("/5")):
                            try:
                                dd = chatdata['5']['data']['16']
                                print('msg in private')
                                message = f"[B][C]{get_random_color()}\n\nAccepT My InV FasT\n\n"
                                P = await SEndMsG(response.Data.chat_type , message , uid , chat_id , key , iv)
                                await SEndPacKeT(whisper_writer , online_writer , 'ChaT' , P)
                                PAc = await OpEnSq(key , iv,region)
                                await SEndPacKeT(whisper_writer , online_writer , 'OnLine' , PAc)
                                C = await cHSq(5, uid ,key, iv,region)
                                await asyncio.sleep(0.5)
                                await SEndPacKeT(whisper_writer , online_writer , 'OnLine' , C)
                                V = await SEnd_InV(5 , uid , key , iv,region)
                                await asyncio.sleep(0.5)
                                await SEndPacKeT(whisper_writer , online_writer , 'OnLine' , V)
                                E = await ExiT(None , key , iv)
                                await asyncio.sleep(3)
                                await SEndPacKeT(whisper_writer , online_writer , 'OnLine' , E)
                            except:
                                print('msg in squad')



                        if inPuTMsG.startswith('/x/'):
                            CodE = inPuTMsG.split('/x/')[1]
                            try:
                                dd = chatdata['5']['data']['16']
                                print('msg in private')
                                EM = await GenJoinSquadsPacket(CodE , key , iv)
                                await SEndPacKeT(whisper_writer , online_writer , 'OnLine' , EM)


                            except:
                                print('msg in squad')

                        if inPuTMsG.startswith('leave'):
                            leave = await ExiT(uid,key,iv)
                            await SEndPacKeT(whisper_writer , online_writer , 'OnLine' , leave)

                        if inPuTMsG.strip().startswith('/s'):
                            EM = await FS(key , iv)
                            await SEndPacKeT(whisper_writer , online_writer , 'OnLine' , EM)


                        if inPuTMsG.strip().startswith('/f'):

                            try:
                                dd = chatdata['5']['data']['16']
                                print('msg in private')
                                message = f"[B][C]{get_random_color()}\n\nOnLy In SQuaD ! \n\n"
                                P = await SEndMsG(response.Data.chat_type, message, uid, chat_id, key, iv)
                                await SEndPacKeT(whisper_writer, online_writer, 'ChaT', P)

                            except:
                                print('msg in squad')

                                parts = inPuTMsG.strip().split()
                                print(response.Data.chat_type, uid, chat_id)
                                message = f'[B][C]{get_random_color()}\nACITVE TarGeT -> {xMsGFixinG(uid)}\n'

                                P = await SEndMsG(response.Data.chat_type, message, uid, chat_id, key, iv)

                                uid2 = uid3 = uid4 = uid5 = uid6 = None
                                s = False

                                try:
                                    uid = int(parts[1])
                                    uid2 = int(parts[2])
                                    uid3 = int(parts[3])
                                    uid4 = int(parts[4])
                                    uid5 = int(parts[5])
                                    uid6 = int(parts[6])
                                    idT = int(parts[6])

                                except ValueError as ve:
                                    print("ValueError:", ve)
                                    s = True

                                except Exception:
                                    idT = len(parts) - 1
                                    idT = int(parts[idT])
                                    print(idT)
                                    print(uid)

                                if not s:
                                    try:
                                        await SEndPacKeT(whisper_writer, online_writer, 'ChaT', P)

                                        # 🚀 Super Fast Emote Loop
                                        for i in range(200):  # repeat count
                                            print(f"Fast Emote {i+1}")
                                            H = await Emote_k(uid, idT, key, iv, region)
                                            await SEndPacKeT(whisper_writer, online_writer, 'OnLine', H)

                                            if uid2:
                                                H = await Emote_k(uid2, idT, key, iv, region)
                                                await SEndPacKeT(whisper_writer, online_writer, 'OnLine', H)
                                            if uid3:
                                                H = await Emote_k(uid3, idT, key, iv, region)
                                                await SEndPacKeT(whisper_writer, online_writer, 'OnLine', H)
                                            if uid4:
                                                H = await Emote_k(uid4, idT, key, iv, region)
                                                await SEndPacKeT(whisper_writer, online_writer, 'OnLine', H)
                                            if uid5:
                                                H = await Emote_k(uid5, idT, key, iv, region)
                                                await SEndPacKeT(whisper_writer, online_writer, 'OnLine', H)
                                            if uid6:
                                                H = await Emote_k(uid6, idT, key, iv, region)
                                                await SEndPacKeT(whisper_writer, online_writer, 'OnLine', H)

                                            await asyncio.sleep(0.08)  # ⚡ super-fast delay

                                    except Exception as e:
                                        print("Fast emote error:", e)

                        if inPuTMsG.strip().startswith('/d'):

                            try:
                                dd = chatdata['5']['data']['16']
                                print('msg in private')
                                message = f"[B][C]{get_random_color()}\n\nOnLy In SQuaD ! \n\n"
                                P = await SEndMsG(response.Data.chat_type, message, uid, chat_id, key, iv)
                                await SEndPacKeT(whisper_writer, online_writer, 'ChaT', P)

                            except:
                                print('msg in squad')

                                parts = inPuTMsG.strip().split()
                                print(response.Data.chat_type, uid, chat_id)
                                message = f'[B][C]{get_random_color()}\nACITVE TarGeT -> {xMsGFixinG(uid)}\n'

                                P = await SEndMsG(response.Data.chat_type, message, uid, chat_id, key, iv)

                                uid2 = uid3 = uid4 = uid5 = uid6 = None
                                s = False

                                try:
                                    uid = int(parts[1])
                                    uid2 = int(parts[2])
                                    uid3 = int(parts[3])
                                    uid4 = int(parts[4])
                                    uid5 = int(parts[5])
                                    uid6 = int(parts[6])
                                    idT = int(parts[6])

                                except ValueError as ve:
                                    print("ValueError:", ve)
                                    s = True

                                except Exception:
                                    idT = len(parts) - 1
                                    idT = int(parts[idT])
                                    print(idT)
                                    print(uid)

                                if not s:
                                    try:
                                        await SEndPacKeT(whisper_writer, online_writer, 'ChaT', P)

                                        H = await Emote_k(uid, idT, key, iv,region)
                                        await SEndPacKeT(whisper_writer, online_writer, 'OnLine', H)

                                        if uid2:
                                            H = await Emote_k(uid2, idT, key, iv,region)
                                            await SEndPacKeT(whisper_writer, online_writer, 'OnLine', H)
                                        if uid3:
                                            H = await Emote_k(uid3, idT, key, iv,region)
                                            await SEndPacKeT(whisper_writer, online_writer, 'OnLine', H)
                                        if uid4:
                                            H = await Emote_k(uid4, idT, key, iv,region)
                                            await SEndPacKeT(whisper_writer, online_writer, 'OnLine', H)
                                        if uid5:
                                            H = await Emote_k(uid5, idT, key, iv,region)
                                            await SEndPacKeT(whisper_writer, online_writer, 'OnLine', H)
                                            if uid6:
                                                H = await Emote_k(uid6, idT, key, iv, region)
                                                await SEndPacKeT(whisper_writer, online_writer, 'OnLine', H)
                                        

                                    except Exception as e:
                                        pass


                        if inPuTMsG in ("dev"):
                            uid = response.Data.uid
                            chat_id = response.Data.Chat_ID
                            message = '/d <uid1> <uid2>... <emoteid> /f <uid1> <uid2>... <emoteid> for fast emote'
                            P = await SEndMsG(response.Data.chat_type , message , uid , chat_id , key , iv)
                            await SEndPacKeT(whisper_writer , online_writer , 'ChaT' , P)
                        response = None
                            
            whisper_writer.close() ; await whisper_writer.wait_closed() ; whisper_writer = None
                    
                    	
                    	
        except Exception as e: print(f"ErroR {ip}:{port} - {e}") ; whisper_writer = None
        await asyncio.sleep(reconnect_delay)

# Dictionary to store bot data per region
class BotInstance:
    def __init__(self, region, uid, password, online_writer, whisper_writer, key, iv, bot_uid, loop):
        self.region = region
        self.uid = uid
        self.password = password
        self.online_writer = online_writer
        self.whisper_writer = whisper_writer
        self.key = key
        self.iv = iv
        self.bot_uid = bot_uid
        self.loop = loop
        self.in_use = False

# ---------------------- FLASK ROUTES ----------------------

loop = None

async def perform_emote_with_bot(bot_instance, team_code: str, uids: list, emote_id: int):
    """Perform emote using a specific bot instance"""
    try:
        if bot_instance.online_writer is None:
            raise Exception(f"Bot {bot_instance.region} not connected")

        # 1. JOIN SQUAD (super fast)
        EM = await GenJoinSquadsPacket(team_code, bot_instance.key, bot_instance.iv)
        await SEndPacKeT(None, bot_instance.online_writer, 'OnLine', EM)
        await asyncio.sleep(0.12)  # minimal sync delay

        # 2. PERFORM EMOTE instantly
        for uid_str in uids:
            target_uid = int(uid_str)
            H = await Emote_k(target_uid, emote_id, bot_instance.key, bot_instance.iv, bot_instance.region)
            await SEndPacKeT(None, bot_instance.online_writer, 'OnLine', H)

        # 3. LEAVE SQUAD instantly (correct bot UID)
        LV = await ExiT(bot_instance.bot_uid, bot_instance.key, bot_instance.iv)
        await SEndPacKeT(None, bot_instance.online_writer, 'OnLine', LV)
        await asyncio.sleep(0.03)

        return {"status": "success", "message": f"Emote done by {bot_instance.region} bot"}
    except Exception as e:
        raise Exception(f"Failed to perform emote with {bot_instance.region} bot: {str(e)}")

@app.route('/join')
def join_team():
    global loop, active_bots
    
    team_code = request.args.get('tc')
    uid1 = request.args.get('uid1')
    uid2 = request.args.get('uid2')
    uid3 = request.args.get('uid3')
    uid4 = request.args.get('uid4')
    uid5 = request.args.get('uid5')
    uid6 = request.args.get('uid6')
    emote_id_str = request.args.get('emote_id')
    region_param = request.args.get('region', '').upper()

    if not team_code or not emote_id_str:
        return jsonify({"status": "error", "message": "Missing tc or emote_id"})

    if not region_param or region_param not in available_regions:
        return jsonify({
            "status": "error", 
            "message": f"Invalid or missing region. Available: {available_regions}"
        })

    try:
        emote_id = int(emote_id_str)
    except:
        return jsonify({"status": "error", "message": "emote_id must be integer"})

    uids = [uid for uid in [uid1, uid2, uid3, uid4, uid5, uid6] if uid]

    if not uids:
        return jsonify({"status": "error", "message": "Provide at least one UID"})

    # Check if region has active bots
    with bot_instances_lock:
        if region_param not in active_bots or not active_bots[region_param]:
            return jsonify({
                "status": "error",
                "message": f"No active bots in region {region_param}. Bot might be starting or disconnected."
            })
        
        # Select random bot from available ones (not in use ideally)
        # For simplicity, just pick first one for now - can be enhanced with round-robin
        available_bots = [bot for bot in active_bots[region_param] if not bot.in_use]
        if not available_bots:
            # If all in use, still pick one (they'll queue)
            bot_instance = random.choice(active_bots[region_param])
        else:
            bot_instance = random.choice(available_bots)
        
        bot_instance.in_use = True

    # Perform emote in background
    async def do_emote():
        try:
            result = await perform_emote_with_bot(bot_instance, team_code, uids, emote_id)
            print(f"Emote completed: {result}")
        except Exception as e:
            print(f"Emote failed: {e}")
        finally:
            bot_instance.in_use = False

    asyncio.run_coroutine_threadsafe(do_emote(), loop)

    return jsonify({
        "status": "success",
        "region": region_param,
        "team_code": team_code,
        "uids": uids,
        "emote_id": emote_id_str,
        "message": f"Emote triggered using {region_param} bot (random from 6 accounts)"
    })

@app.route('/regions')
def list_regions():
    """Endpoint to check available regions and bot status"""
    with bot_instances_lock:
        status = {}
        for region in available_regions:
            if region in active_bots and active_bots[region]:
                status[region] = {
                    "active": True,
                    "bot_count": len(active_bots[region]),
                    "available": len([b for b in active_bots[region] if not b.in_use])
                }
            else:
                status[region] = {"active": False, "bot_count": 0}
    
    return jsonify({
        "available_regions": available_regions,
        "bot_status": status
    })

def run_flask():
    port = int(os.environ.get("PORT", 10000))
    app.run(host='0.0.0.0', port=port, debug=False, use_reloader=False)


# ---------------------- MAIN BOT SYSTEM ----------------------

async def run_single_bot(region, account_index):
    """Run a single bot instance for a specific region and account"""
    global loop, active_bots
    
    uid, password = region_accounts[region][account_index]
    
    print(f"Starting bot for {region} - Account {account_index+1}: {uid}")
    
    open_id, access_token = await GeNeRaTeAccEss(uid, password)
    if not open_id or not access_token:
        print(f"ErroR - InvaLid AccounT for {region} - {uid}")
        return None

    PyL = await EncRypTMajoRLoGin(open_id, access_token)
    MajoRLoGinResPonsE = await MajorLogin(PyL)
    if not MajoRLoGinResPonsE:
        print(f"TarGeT AccounT => BannEd / NoT ReGisTeReD ! for {region} - {uid}")
        return None

    MajoRLoGinauTh = await DecRypTMajoRLoGin(MajoRLoGinResPonsE)
    UrL = MajoRLoGinauTh.url
    bot_region = MajoRLoGinauTh.region

    ToKen = MajoRLoGinauTh.token
    bot_uid = MajoRLoGinauTh.account_uid
    key = MajoRLoGinauTh.key
    iv = MajoRLoGinauTh.iv
    timestamp = MajoRLoGinauTh.timestamp

    LoGinDaTa = await GetLoginData(UrL, PyL, ToKen)
    if not LoGinDaTa:
        print(f"ErroR - GeTinG PorTs From LoGin DaTa for {region} - {uid}")
        return None

    LoGinDaTaUncRypTinG = await DecRypTLoGinDaTa(LoGinDaTa)
    OnLinePorTs = LoGinDaTaUncRypTinG.Online_IP_Port
    ChaTPorTs = LoGinDaTaUncRypTinG.AccountIP_Port

    OnLineiP, OnLineporT = OnLinePorTs.split(":")
    ChaTiP, ChaTporT = ChaTPorTs.split(":")

    acc_name = LoGinDaTaUncRypTinG.AccountName

    AutHToKen = await xAuThSTarTuP(int(bot_uid), ToKen, int(timestamp), key, iv)
    ready_event = asyncio.Event()

    # Store bot instance reference
    bot_instance = BotInstance(region, uid, password, None, None, key, iv, bot_uid, loop)
    
    with bot_instances_lock:
        if region not in active_bots:
            active_bots[region] = []
        active_bots[region].append(bot_instance)

    # TCP Chat Task
    async def run_chat():
        nonlocal bot_instance
        reader, writer = await asyncio.open_connection(ChaTiP, int(ChaTporT))
        bot_instance.whisper_writer = writer
        bytes_payload = bytes.fromhex(AutHToKen)
        bot_instance.whisper_writer.write(bytes_payload)
        await bot_instance.whisper_writer.drain()
        ready_event.set()
        
        if LoGinDaTaUncRypTinG.Clan_ID:
            clan_id = LoGinDaTaUncRypTinG.Clan_ID
            clan_compiled_data = LoGinDaTaUncRypTinG.Clan_Compiled_Data
            pK = await AuthClan(clan_id, clan_compiled_data, key, iv)
            if bot_instance.whisper_writer:
                bot_instance.whisper_writer.write(pK)
                await bot_instance.whisper_writer.drain()
        
        # Keep connection alive
        while True:
            try:
                await asyncio.sleep(30)
            except:
                break

    # TCP Online Task
    async def run_online():
        nonlocal bot_instance
        reader, writer = await asyncio.open_connection(OnLineiP, int(OnLineporT))
        bot_instance.online_writer = writer
        bytes_payload = bytes.fromhex(AutHToKen)
        bot_instance.online_writer.write(bytes_payload)
        await bot_instance.online_writer.drain()
        
        while True:
            try:
                await asyncio.sleep(30)
            except:
                break

    # Start both tasks
    chat_task = asyncio.create_task(run_chat())
    online_task = asyncio.create_task(run_online())
    
    await ready_event.wait()
    await asyncio.sleep(1)
    
    print(f"✓ Bot online: {region} | UID: {bot_uid} | Name: {acc_name}")
    
    # Keep tasks running
    await asyncio.gather(chat_task, online_task)

async def MaiiiinE():
    global loop
    
    loop = asyncio.get_running_loop()
    
    # Start Flask in thread
    flask_thread = threading.Thread(target=run_flask, daemon=True)
    flask_thread.start()
    
    os.system('clear')
    print(render('MULTI-REGION BOT', colors=['white', 'green'], align='center'))
    print(f"\nAvailable Regions: {available_regions}")
    print("Starting all region bots...\n")
    
    # Start all bots for all regions (6 accounts each)
    bot_tasks = []
    for region in available_regions:
        for i in range(6):  # 6 accounts per region
            bot_tasks.append(asyncio.create_task(run_single_bot(region, i)))
            await asyncio.sleep(2)  # Small delay to avoid rate limiting
    
    print(f"\n✓ Total bots started: {len(bot_tasks)}")
    print("✓ Flask API running on port 10000")
    print("✓ Use: /join?tc=CODE&uid1=UID&emote_id=ID&region=IND\n")
    
    await asyncio.gather(*bot_tasks)


async def StarTinG():
    while True:
        try:
            await asyncio.wait_for(MaiiiinE(), timeout=7 * 60 * 60)
        except asyncio.TimeoutError:
            print("Token ExpiRed! Restarting all bots...")
        except Exception as e:
            print(f"ErroR - {e} => Restarting all bots...")


if __name__ == '__main__':
    asyncio.run(StarTinG())