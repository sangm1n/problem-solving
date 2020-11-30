/*
16진수로 입력된 정수 1개를 8진수로 바꾸어 출력해보자.
 */

import java.util.Scanner;

public class Prob1035 {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);

        String input = scan.nextLine();
        int num = Integer.parseInt(input, 16);
        System.out.printf("%o", num);
    }
}
