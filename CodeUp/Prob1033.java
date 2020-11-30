/*
10진수를 입력받아 16진수(hexadecimal)로 출력해보자.
%X로 출력하면 16진수(hexadecimal) 대문자로 출력된다.
 */

import java.util.Scanner;

public class Prob1033 {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);

        int num = scan.nextInt();
        System.out.printf("%X", num);
    }
}
