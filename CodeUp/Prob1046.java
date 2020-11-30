/*
정수 3개를 입력받아 합과 평균을 출력해보자.
단, -2147483648 ~ +2147483647
 */

import java.util.Scanner;

public class Prob1046 {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);

        float a = scan.nextFloat();
        float b = scan.nextFloat();
        float c = scan.nextFloat();

        System.out.println((long)(a + b + c));
        System.out.printf("%.1f", (a+b+c)/3);
    }
}
