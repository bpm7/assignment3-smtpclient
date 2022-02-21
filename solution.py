from socket import *


def smtp_client(port=1025, mailserver='127.0.0.1'):
    msg = "\r\n Brian Murphy Spring 2022 Messaging system"
    endmsg = "\r\n.\r\n"

    # Choose a mail server (e.g. Google mail server) if you want to verify the script beyond GradeScope

    # Create socket called clientSocket and establish a TCP connection with mailserver and port

    # Fill in start
    clientSocket=socket(AF_INET,SOCK_STREAM)
    clientSocket.connect((mailserver,port))
    # Fill in end

    recv = clientSocket.recv(1024).decode()
    #print(recv) #You can use these print statement to validate return codes from the server.
    #if recv[:3] != '220':
    #    print('220 reply not received from server.')

    # Send HELO command and print server response.
    heloCommand = 'HELO Alice\r\n'
    clientSocket.send(heloCommand.encode())
    recv1 = clientSocket.recv(1024).decode()
    #print(recv1) 
    if recv1[:3] != '250':
        print('250 reply not received from server.')

    # Send MAIL FROM command and handle server response.
    #print("Sending Mail")
    # Fill in start
    mailFromCommand='MAIL FROM: <brian@murphy.compnet.spring22>\r\n'
    clientSocket.send(mailFromCommand.encode())
    recv1 = clientSocket.recv(1024).decode()
    #print(recv1)
    if recv1[:3] != '250':
        print('250 reply not received from server on MAIL FROM.')
    # Fill in end

    # Send RCPT TO command and handle server response.
    #print("Sending RCPT")
    # Fill in start
    rcptToCommand='RCPT TO: <debugger@local.net>\r\n'
    clientSocket.send(rcptToCommand.encode())
    recv1 = clientSocket.recv(1024).decode()
    #print(recv1)
    if recv1[:3] != '250':
        print('250 reply not received from server on RCPT TO.')
    # Fill in end

    # Send DATA command and handle server response.
    #print("Sending DATA")
    # Fill in start
    data='DATA\r\n'
    clientSocket.send(data.encode())
    recv1 = clientSocket.recv(1024).decode()
    #print(recv1)
    if recv1[:3] != '354':
        print('250 reply not received from server on DATA.')
    # Fill in end

    # Send message data.
    oneLine='Hello this is Brian Murphy.\r\n'
    twoLine='I am taking Computer Networking Spring 2022\r\n'
    threeLine='I am a Staff Analyst for the NYC Gov'
    fourLine=''' This is a test of a multi line with email sending.
    I am not sure this will work.
    Hoping for the best!\r\n
    '''
    myDataLines=[oneLine]# twoLine,threeLine,fourLine]
    #print("Sending Dat Lines")
    clientSocket.send(msg.encode())

    #for i in myDataLines:
    #    print(i)
    #    clientSocket.send(i.encode())
    #    recv1 = clientSocket.recv(1024).decode()
    #    print(recv1)
    #    if recv1[:3] != '250':
    #        print('250 reply not received from server on Data sending at:'+i)

    
    # Fill in start
    # Fill in end

    # Message ends with a single period, send message end and handle server response.
    # Fill in start
    #print("Sending END")
    clientSocket.send(endmsg.encode())
    recv1 = clientSocket.recv(1024).decode()
    #print(recv1)
    if recv1[:3] != '250':
        print('250 reply not received from server on DATA End.')
    # Fill in end

    # Send QUIT command and handle server response.
    # Fill in start
    #print("Sending QUIT")
    quitCommand='QUIT\r\n'
    clientSocket.send(quitCommand.encode())
    recv1 = clientSocket.recv(1024).decode()
    #print(recv1)
    if recv1[:3] != '221':
        print('221 reply not received from server on QUIT.')
    # Fill in end


if __name__ == '__main__':
    smtp_client(1025, '127.0.0.1')