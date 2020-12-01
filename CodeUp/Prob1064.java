/*
입력된 세 정수 a, b, c 중 가장 작은 값을 출력하는 프로그램을 작성해보자.
단, 조건문을 사용하지 않고 3항 연산자 ? 를 사용한다.
 */

import java.util.Scanner;

public class Prob1064 {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);

        int a = scan.nextInt();
        int b = scan.nextInt();
        int c = scan.nextInt();

        int result = (a < b) ? a : b;
        result = (result < c) ? result: c;
        System.out.println(result);
    }
}
