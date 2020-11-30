/*
int형 정수 1개를 입력받아 공백을 사이에 두고 3번 출력해보자.
 */

import java.util.*;

public class Prob1017 {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);

        int num = scan.nextInt();
        System.out.println(num + " " + num + " " + num);
    }
}
