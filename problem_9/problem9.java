
public class problem9 {
	public static boolean isTriangle(int a, int b, int c) {
		if(a + b > c && a + c > b && b + c > a) {
			return true;
		}
		return false;
	}

	public static boolean isTriplet(int a, int b, int c) {
		if(a * a + b * b == c * c) {
			return true;
		}
		return false;
	}

	public static void main(String[] args) {
		for(int a = 1; a < 1_001; a++) {
			for(int b = 1; b < 1_001; b++) {
				for(int c = 1; c < 1_001; c++) {
					if(isTriangle(a, b, c) && isTriplet(a, b, c) && a + b + c == 1_000) {
						System.out.print(a * b * c);
					}
				}
			}
		}
	}
}