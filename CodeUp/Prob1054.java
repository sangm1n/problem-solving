/*
두 개의 참(1) 또는 거짓(0)이 입력될 때,
모두 참일 때에만 참을 출력하는 프로그램을 작성해보자.
 */

import java.util.Scanner;

public class Prob1054 {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);

        int a = scan.nextInt();
        int b = scan.nextInt();

        if (a == 1 && b == 1) {
            System.out.println(1);
        } else {
            System.out.println(0);
        }
    }
}
