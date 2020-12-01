/*
정수(0 ~ 100) 1개를 입력받아 0부터 그 수까지 순서대로 출력해보자.
 */

import java.util.Scanner;

public class Prob1077 {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);

        int num = scan.nextInt();

        for (int i = 0; i < num+1; i++) {
            System.out.println(i);
        }
    }
}
