/*
실수(float) 1개를 입력받아 저장한 후,
저장되어 있는 값을 소수점 셋 째 자리에서 반올림하여
소수점 이하 둘 째 자리까지 출력하시오.
 */

import java.util.*;

public class Prob1015 {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);

        String input = scan.nextLine();
        float f = Float.parseFloat(input);
        System.out.printf("%.2f", f);
    }
}
