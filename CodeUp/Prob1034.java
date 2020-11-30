/*
8진수로 입력된 정수 1개를 10진수로 바꾸어 출력해보자.
 */

import java.util.Scanner;

public class Prob1034 {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);

        String input = scan.nextLine();
        int num = Integer.parseInt(input, 8);
        System.out.printf("%d", num);
    }
}
