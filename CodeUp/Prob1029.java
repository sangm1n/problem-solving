/*
실수 1개를 입력받아 그대로 출력해보자.
(단, 입력되는 실수의 범위는 +- 1.7*10^-308 ~ +- 1.7*10^308 이다.)
 */

import java.util.*;

public class Prob1029 {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);

        double num = scan.nextDouble();
        System.out.printf("%.11f", num);
    }
}
