/*
영문자 1개를 입력받아 아스키 코드표의 10진수 값으로 출력해보자.
 */

import java.util.Scanner;

public class Prob1036 {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);

        char ch = scan.next().charAt(0);
        System.out.println((int)ch);
    }
}
