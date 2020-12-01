/*
두 정수(a, b)를 입력받아
a와 b가 서로 다르면 1을, 그렇지 않으면 0을 출력하는 프로그램을 작성해보자.
 */

import java.util.Scanner;

public class Prob1052 {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);

        int a = scan.nextInt();
        int b = scan.nextInt();

        int result = (a != b) ? 1 : 0;
        System.out.println(result);
    }
}
