import csv
import sys


def generate_putty_session_file(csv_file, session_file):
    data = []
    with open(csv_file, 'r') as file:
        csv_data = csv.DictReader(file)
        # Convert CSV data to a list of dictionaries
        for row in csv_data:
            data.append(row)
    # Create the session file
    with open(session_file, 'w') as file:
        file.write('REGEDIT4\n\n')
        for session in data:
            section_name = session.get('SessionName')
            host_name = session.get('HostName')
            file.write(f'[HKEY_CURRENT_USER\Software\SimonTatham\PuTTY\Sessions\{section_name}]\n')
            file.write(f'"Present"=dword:00000001\n')
            file.write(f'"HostName"="{host_name}"\n')
            file.write(f'"LogFileName"="putty.log"\n')
            file.write(f'"LogType"=dword:00000000\n')
            file.write(f'"LogFileClash"=dword:ffffffff\n')
            file.write(f'"LogFlush"=dword:00000001\n')
            file.write(f'"LogHeader"=dword:00000001\n')
            file.write(f'"SSHLogOmitPasswords"=dword:00000001\n')
            file.write(f'"SSHLogOmitData"=dword:00000000\n')
            file.write(f'"Protocol"="ssh"\n')
            file.write(f'"PortNumber"=dword:00000016\n')
            file.write(f'"CloseOnExit"=dword:00000001\n')
            file.write(f'"WarnOnClose"=dword:00000001\n')
            file.write(f'"PingInterval"=dword:00000000\n')
            file.write(f'"PingIntervalSecs"=dword:00000000\n')
            file.write(f'"TCPNoDelay"=dword:00000001\n')
            file.write(f'"TCPKeepalives"=dword:00000000\n')
            file.write(f'"TerminalType"="xterm"\n')
            file.write(f'"TerminalSpeed"="38400,38400"\n')
            file.write(
                f'"TerminalModes"="CS7=A,CS8=A,DISCARD=A,DSUSP=A,ECHO=A,ECHOCTL=A,ECHOE=A,ECHOK=A,ECHOKE=A,ECHONL=A,EOF=A,EOL=A,EOL2=A,ERASE=A,FLUSH=A,ICANON=A,ICRNL=A,IEXTEN=A,IGNCR=A,IGNPAR=A,IMAXBEL=A,INLCR=A,INPCK=A,INTR=A,ISIG=A,ISTRIP=A,IUCLC=A,IUTF8=A,IXANY=A,IXOFF=A,IXON=A,KILL=A,LNEXT=A,NOFLSH=A,OCRNL=A,OLCUC=A,ONLCR=A,ONLRET=A,ONOCR=A,OPOST=A,PARENB=A,PARMRK=A,PARODD=A,PENDIN=A,QUIT=A,REPRINT=A,START=A,STATUS=A,STOP=A,SUSP=A,SWTCH=A,TOSTOP=A,WERASE=A,XCASE=A"\n')
            file.write(f'"AddressFamily"=dword:00000000\n')
            file.write(f'"ProxyExcludeList"=""\n')
            file.write(f'"ProxyDNS"=dword:00000001\n')
            file.write(f'"ProxyLocalhost"=dword:00000000\n')
            file.write(f'"ProxyMethod"=dword:00000000\n')
            file.write(f'"ProxyHost"="proxy"\n')
            file.write(f'"ProxyPort"=dword:00000050\n')
            file.write(f'"ProxyUsername"=""\n')
            file.write(f'"ProxyPassword"=""\n')
            file.write(f'"ProxyTelnetCommand"="connect %host %port\\n"\n')
            file.write(f'"ProxyLogToTerm"=dword:00000001\n')
            file.write(f'"Environment"=""\n')
            file.write(f'"UserName"=""\n')
            file.write(f'"UserNameFromEnvironment"=dword:00000000\n')
            file.write(f'"LocalUserName"=""\n')
            file.write(f'"NoPTY"=dword:00000000\n')
            file.write(f'"Compression"=dword:00000000\n')
            file.write(f'"TryAgent"=dword:00000001\n')
            file.write(f'"AgentFwd"=dword:00000000\n')
            file.write(f'"GssapiFwd"=dword:00000000\n')
            file.write(f'"ChangeUsername"=dword:00000000\n')
            file.write(f'"Cipher"="aes,chacha20,aesgcm,3des,WARN,des,blowfish,arcfour"\n')
            file.write(
                f'"KEX"="ntru-curve25519,ecdh,dh-gex-sha1,dh-group18-sha512,dh-group17-sha512,dh-group16-sha512,dh-group15-sha512,dh-group14-sha1,rsa,WARN,dh-group1-sha1"\n')
            file.write(f'"HostKey"="ed448,ed25519,ecdsa,rsa,dsa,WARN"\n')
            file.write(f'"PreferKnownHostKeys"=dword:00000001\n')
            file.write(f'"RekeyTime"=dword:0000003c\n')
            file.write(f'"GssapiRekey"=dword:00000002\n')
            file.write(f'"RekeyBytes"="1G"\n')
            file.write(f'"SshNoAuth"=dword:00000000\n')
            file.write(f'"SshNoTrivialAuth"=dword:00000000\n')
            file.write(f'"SshBanner"=dword:00000001\n')
            file.write(f'"AuthTIS"=dword:00000000\n')
            file.write(f'"AuthKI"=dword:00000001\n')
            file.write(f'"AuthGSSAPI"=dword:00000001\n')
            file.write(f'"AuthGSSAPIKEX"=dword:00000001\n')
            file.write(f'"GSSLibs"="gssapi32,sspi,custom"\n')
            file.write(f'"GSSCustom"=""\n')
            file.write(f'"SshNoShell"=dword:00000000\n')
            file.write(f'"SshProt"=dword:00000003\n')
            file.write(f'"LogHost"=""\n')
            file.write(f'"SSH2DES"=dword:00000000\n')
            file.write(f'"PublicKeyFile"=""\n')
            file.write(f'"DetachedCertificate"=""\n')
            file.write(f'"AuthPlugin"=""\n')
            file.write(f'"RemoteCommand"=""\n')
            file.write(f'"RFCEnviron"=dword:00000000\n')
            file.write(f'"PassiveTelnet"=dword:00000000\n')
            file.write(f'"BackspaceIsDelete"=dword:00000001\n')
            file.write(f'"RXVTHomeEnd"=dword:00000000\n')
            file.write(f'"LinuxFunctionKeys"=dword:00000000\n')
            file.write(f'"ShiftedArrowKeys"=dword:00000000\n')
            file.write(f'"NoApplicationKeys"=dword:00000000\n')
            file.write(f'"NoApplicationCursors"=dword:00000000\n')
            file.write(f'"NoMouseReporting"=dword:00000000\n')
            file.write(f'"NoRemoteResize"=dword:00000000\n')
            file.write(f'"NoAltScreen"=dword:00000000\n')
            file.write(f'"NoRemoteWinTitle"=dword:00000000\n')
            file.write(f'"NoRemoteClearScroll"=dword:00000000\n')
            file.write(f'"RemoteQTitleAction"=dword:00000001\n')
            file.write(f'"NoDBackspace"=dword:00000000\n')
            file.write(f'"NoRemoteCharset"=dword:00000000\n')
            file.write(f'"ApplicationCursorKeys"=dword:00000000\n')
            file.write(f'"ApplicationKeypad"=dword:00000000\n')
            file.write(f'"NetHackKeypad"=dword:00000000\n')
            file.write(f'"AltF4"=dword:00000001\n')
            file.write(f'"AltSpace"=dword:00000000\n')
            file.write(f'"AltOnly"=dword:00000000\n')
            file.write(f'"ComposeKey"=dword:00000000\n')
            file.write(f'"CtrlAltKeys"=dword:00000001\n')
            file.write(f'"TelnetKey"=dword:00000000\n')
            file.write(f'"TelnetRet"=dword:00000001\n')
            file.write(f'"LocalEcho"=dword:00000002\n')
            file.write(f'"LocalEdit"=dword:00000002\n')
            file.write(f'"Answerback"="PuTTY"\n')
            file.write(f'"AlwaysOnTop"=dword:00000000\n')
            file.write(f'"FullScreenOnAltEnter"=dword:00000000\n')
            file.write(f'"HideMousePtr"=dword:00000000\n')
            file.write(f'"SunkenEdge"=dword:00000000\n')
            file.write(f'"WindowBorder"=dword:00000001\n')
            file.write(f'"CurType"=dword:00000000\n')
            file.write(f'"BlinkCur"=dword:00000000\n')
            file.write(f'"Beep"=dword:00000001\n')
            file.write(f'"BeepInd"=dword:00000000\n')
            file.write(f'"BellWaveFile"=""\n')
            file.write(f'"BellOverload"=dword:00000001\n')
            file.write(f'"BellOverloadN"=dword:00000005\n')
            file.write(f'"BellOverloadT"=dword:000007d0\n')
            file.write(f'"BellOverloadS"=dword:00001388\n')
            file.write(f'"ScrollbackLines"=dword:000007d0\n')
            file.write(f'"DECOriginMode"=dword:00000000\n')
            file.write(f'"AutoWrapMode"=dword:00000001\n')
            file.write(f'"LFImpliesCR"=dword:00000000\n')
            file.write(f'"CRImpliesLF"=dword:00000000\n')
            file.write(f'"DisableArabicShaping"=dword:00000000\n')
            file.write(f'"DisableBidi"=dword:00000000\n')
            file.write(f'"WinNameAlways"=dword:00000001\n')
            file.write(f'"WinTitle"=""\n')
            file.write(f'"TermWidth"=dword:00000050\n')
            file.write(f'"TermHeight"=dword:00000018\n')
            file.write(f'"Font"="Courier New"\n')
            file.write(f'"FontIsBold"=dword:00000000\n')
            file.write(f'"FontCharSet"=dword:00000000\n')
            file.write(f'"FontHeight"=dword:0000000a\n')
            file.write(f'"FontQuality"=dword:00000000\n')
            file.write(f'"FontVTMode"=dword:00000004\n')
            file.write(f'"UseSystemColours"=dword:00000000\n')
            file.write(f'"TryPalette"=dword:00000000\n')
            file.write(f'"ANSIColour"=dword:00000001\n')
            file.write(f'"Xterm256Colour"=dword:00000001\n')
            file.write(f'"TrueColour"=dword:00000001\n')
            file.write(f'"BoldAsColour"=dword:00000001\n')
            file.write(f'"Colour0"="187,187,187"\n')
            file.write(f'"Colour1"="255,255,255"\n')
            file.write(f'"Colour2"="0,0,0"\n')
            file.write(f'"Colour3"="85,85,85"\n')
            file.write(f'"Colour4"="0,0,0"\n')
            file.write(f'"Colour5"="0,255,0"\n')
            file.write(f'"Colour6"="0,0,0"\n')
            file.write(f'"Colour7"="85,85,85"\n')
            file.write(f'"Colour8"="187,0,0"\n')
            file.write(f'"Colour9"="255,85,85"\n')
            file.write(f'"Colour10"="0,187,0"\n')
            file.write(f'"Colour11"="85,255,85"\n')
            file.write(f'"Colour12"="187,187,0"\n')
            file.write(f'"Colour13"="255,255,85"\n')
            file.write(f'"Colour14"="0,0,187"\n')
            file.write(f'"Colour15"="85,85,255"\n')
            file.write(f'"Colour16"="187,0,187"\n')
            file.write(f'"Colour17"="255,85,255"\n')
            file.write(f'"Colour18"="0,187,187"\n')
            file.write(f'"Colour19"="85,255,255"\n')
            file.write(f'"Colour20"="187,187,187"\n')
            file.write(f'"Colour21"="255,255,255"\n')
            file.write(f'"RawCNP"=dword:00000000\n')
            file.write(f'"UTF8linedraw"=dword:00000000\n')
            file.write(f'"PasteRTF"=dword:00000000\n')
            file.write(f'"MouseIsXterm"=dword:00000000\n')
            file.write(f'"RectSelect"=dword:00000000\n')
            file.write(f'"PasteControls"=dword:00000000\n')
            file.write(f'"MouseOverride"=dword:00000001\n')
            file.write(f'"Wordness0"="0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0"\n')
            file.write(f'"Wordness32"="0,1,2,1,1,1,1,1,1,1,1,1,1,2,2,2,2,2,2,2,2,2,2,2,2,2,1,1,1,1,1,1"\n')
            file.write(f'"Wordness64"="1,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,1,1,1,1,2"\n')
            file.write(f'"Wordness96"="1,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,1,1,1,1,1"\n')
            file.write(f'"Wordness128"="1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1"\n')
            file.write(f'"Wordness160"="1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1"\n')
            file.write(f'"Wordness192"="2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,1,2,2,2,2,2,2,2,2"\n')
            file.write(f'"Wordness224"="2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,1,2,2,2,2,2,2,2,2"\n')
            file.write(f'"MouseAutocopy"=dword:00000001\n')
            file.write(f'"MousePaste"="explicit"\n')
            file.write(f'"CtrlShiftIns"="explicit"\n')
            file.write(f'"CtrlShiftCV"="none"\n')
            file.write(f'"LineCodePage"=""\n')
            file.write(f'"CJKAmbigWide"=dword:00000000\n')
            file.write(f'"UTF8Override"=dword:00000001\n')
            file.write(f'"Printer"=""\n')
            file.write(f'"CapsLockCyr"=dword:00000000\n')
            file.write(f'"ScrollBar"=dword:00000001\n')
            file.write(f'"ScrollBarFullScreen"=dword:00000000\n')
            file.write(f'"ScrollOnKey"=dword:00000000\n')
            file.write(f'"ScrollOnDisp"=dword:00000001\n')
            file.write(f'"EraseToScrollback"=dword:00000001\n')
            file.write(f'"LockSize"=dword:00000000\n')
            file.write(f'"BCE"=dword:00000001\n')
            file.write(f'"BlinkText"=dword:00000000\n')
            file.write(f'"X11Forward"=dword:00000000\n')
            file.write(f'"X11Display"=""\n')
            file.write(f'"X11AuthType"=dword:00000001\n')
            file.write(f'"X11AuthFile"=""\n')
            file.write(f'"LocalPortAcceptAll"=dword:00000000\n')
            file.write(f'"RemotePortAcceptAll"=dword:00000000\n')
            file.write(f'"PortForwardings"=""\n')
            file.write(f'"BugIgnore1"=dword:00000000\n')
            file.write(f'"BugPlainPW1"=dword:00000000\n')
            file.write(f'"BugRSA1"=dword:00000000\n')
            file.write(f'"BugIgnore2"=dword:00000000\n')
            file.write(f'"BugHMAC2"=dword:00000000\n')
            file.write(f'"BugDeriveKey2"=dword:00000000\n')
            file.write(f'"BugRSAPad2"=dword:00000000\n')
            file.write(f'"BugPKSessID2"=dword:00000000\n')
            file.write(f'"BugRekey2"=dword:00000000\n')
            file.write(f'"BugMaxPkt2"=dword:00000000\n')
            file.write(f'"BugOldGex2"=dword:00000000\n')
            file.write(f'"BugWinadj"=dword:00000000\n')
            file.write(f'"BugChanReq"=dword:00000000\n')
            file.write(f'"BugDropStart"=dword:00000001\n')
            file.write(f'"BugFilterKexinit"=dword:00000001\n')
            file.write(f'"StampUtmp"=dword:00000001\n')
            file.write(f'"LoginShell"=dword:00000001\n')
            file.write(f'"ScrollbarOnLeft"=dword:00000000\n')
            file.write(f'"BoldFont"=""\n')
            file.write(f'"BoldFontIsBold"=dword:00000000\n')
            file.write(f'"BoldFontCharSet"=dword:00000000\n')
            file.write(f'"BoldFontHeight"=dword:00000000\n')
            file.write(f'"WideFont"=""\n')
            file.write(f'"WideFontIsBold"=dword:00000000\n')
            file.write(f'"WideFontCharSet"=dword:00000000\n')
            file.write(f'"WideFontHeight"=dword:00000000\n')
            file.write(f'"WideBoldFont"=""\n')
            file.write(f'"WideBoldFontIsBold"=dword:00000000\n')
            file.write(f'"WideBoldFontCharSet"=dword:00000000\n')
            file.write(f'"WideBoldFontHeight"=dword:00000000\n')
            file.write(f'"ShadowBold"=dword:00000000\n')
            file.write(f'"ShadowBoldOffset"=dword:00000001\n')
            file.write(f'"SerialLine"="COM1"\n')
            file.write(f'"SerialSpeed"=dword:00002580\n')
            file.write(f'"SerialDataBits"=dword:00000008\n')
            file.write(f'"SerialStopHalfbits"=dword:00000002\n')
            file.write(f'"SerialParity"=dword:00000000\n')
            file.write(f'"SerialFlowControl"=dword:00000001\n')
            file.write(f'"WindowClass"=""\n')
            file.write(f'"ConnectionSharing"=dword:00000000\n')
            file.write(f'"ConnectionSharingUpstream"=dword:00000001\n')
            file.write(f'"ConnectionSharingDownstream"=dword:00000001\n')
            file.write(f'"SSHManualHostKeys"=""\n')
            file.write(f'"SUPDUPLocation"="TheInternet"\n')
            file.write(f'"SUPDUPCharset"=dword:00000000\n')
            file.write(f'"SUPDUPMoreProcessing"=dword:00000000\n')
            file.write(f'"SUPDUPScrolling"=dword:00000000\n')


if __name__ == "__main__":
    csv_file = sys.argv[1]
    session_file = sys.argv[2]
    generate_putty_session_file(csv_file, session_file)