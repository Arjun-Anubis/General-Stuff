#include <stdio.h>
#include <string.h>
#include <windows.h>
#include <winsock.h>
#include <errno.h>


WSADATA wsa;




char to_send;

int main(int argc, char ** argv){
	
	
	if( WSAStartup(MAKEWORD(2,2), &wsa) != 0 ) {
		printf("Error Starting WSA...\n");
	}


	SOCKET s;


	if ((s = socket(AF_INET, SOCK_STREAM, 0)) < 0) {
		printf("Error making socket...\n");
		return 1;
	
	}

	struct sockaddr_in addr;
	memset( &addr, 0, sizeof(addr));
	addr.sin_family = AF_INET;
	addr.sin_port = htons(5001);
	addr.sin_addr.s_addr = inet_addr("15.206.88.194");

	if (connect(s, (struct sockaddr *) &addr, sizeof(addr)) < 0) {
		return 1;
		}

	while (1) {
		read(0, &to_send, sizeof(to_send));
		send(s, &to_send, sizeof(to_send), 0);
	}
	

}
