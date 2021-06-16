#include <stdio.h>
#include <string.h>
#include <windows.h>
#include <winsock.h>
#include <errno.h>

WSADATA wsa;

char recved;
int main(int C, char **V)
{
	SOCKET s, t;
	struct sockaddr_in A;
	

	if( WSAStartup(MAKEWORD(2,2), &wsa) != 0 ) {
		printf("Error WSA\n");
	}

	s = socket(AF_INET, SOCK_STREAM, 0);
	if (s <0) {
		printf("#Error initializing socket...\n#Aborting...");
	}

	memset( &A, 0, sizeof(A) );
	A.sin_family = AF_INET;
	A.sin_port = htons(5000);
	A.sin_addr.s_addr = inet_addr("15.206.88.194");

	if( connect(s, (struct sockaddr *)&A, sizeof(A)) < 0 ) {
		printf("#Failed to connect...\n#Aborting...");
		return 1;
	}
	printf("#Connected\n#Awaiting Input...\n\n");
	
	while (1) {	
	recv(s, &recved, 1, 0);
	write(1, &recved, sizeof(recved));
	}
	
	



	return 0;
}
