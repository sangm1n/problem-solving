/*
정수(1 ~ 100) 1개가 입력되었을 때 카운트다운을 출력해보자.
 */

import java.util.Scanner;

public class Prob1074 {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);

        int num = scan.nextInt();

        for (int i = num; i > 0; i--) {
            System.out.println(i);
        }
    }
}
