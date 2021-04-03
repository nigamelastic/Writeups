public class  jack{
   ;
    String ans1;
    String ans2;
    String ans3;
    
    int click;
    int right = 0;

   
	public static void main(String[] args) {
		System.out.println("Starting_________________________________________________");
        jack jack1= new jack();
        jack1.fun("VGA");
        System.out.println("done");
	}

    

    public void fun(String ans6) {
        if (ans6.equals("VGA")) {
            this.click = 2;
            return;
        }
        int i = this.click;
        if (i == 1) {
            this.ans1 = ab(ans6);
              System.out.println("HDMI least fave");
        } else if (i == 2) {
            this.ans1="EGIKMOQSUW";
            this.ans2 = bc(this.ans1, ans6);
             System.out.println("S-vid 2nd best");
             System.out.println(this.ans2);
        } else if (i >= 3) {
            String ca = ca(this.ans1, this.ans2, ans6);
            this.ans3 = ca;
            if (comp(ans6, ca)) {
                  System.out.println("my code:" + this.ans3);
            } else {
               System.out.println( "Caek? I'm the best ");
            }
            this.click = 0;
        }
    }

    public String ca(String a, String b, String c) {
        char[] a1 = a.toCharArray();
        char[] b1 = b.toCharArray();
        char[] d = new char[6];
        for (int i = 0; i < b.length(); i++) {
            d[i] = (char) ((b1[i] - a1[i]) + 75);
            this.right++;
        }
        int i2 = this.right;
        d[5] = (char) (i2 + 48);
        d[2] = (char) ((i2 / 2) + 48);
        return String.valueOf(d);
    }

    public String bc(String a, String b) {
        char[] aa1 = a.substring(b.length(), a.length()).toCharArray();
        char[] b1 = b.toCharArray();
        char[] c = new char[5];
        for (int i = 0; i < b.length(); i++) {
            char d = aa1[i];
            aa1[i] = aa1[i * 2];
            aa1[i * 2] = d;
        }
        boolean flag = true;
        int i2 = 0;
        while (true) {
            if (i2 >= 3) {
                break;
            } else if (b1[i2] != aa1[i2]) {
               System.out.println("your length matters else it will crash");
                flag = false;
                break;
            } else {
                i2++;
            }
        }
        if (flag) {
            this.right--;
            c[4] = 'I';
            c[0] = 'I';
            c[1] = (char) (c[0] + 5);
            c[2] = (char) (c[0] - 1);
            c[3] = (char) (c[1] + '\t');
        } else {
            c[0] = '1';
        }
        return String.valueOf(c);
    }

    public String ab(String a) {
        char[] a1 = a.toCharArray();
        char[] c = new char[10];
        if (a.length() < 10) {
            System.out.println("the solution is to nullify itself");
            this.click = 1;
            return "0";
        }
        for (int i = 0; i < 10; i++) {
            c[i] = (char) ((i * 2) + 65 + 4);
            if (a1[i] != a1[i + 1] || i + 1 >= a.length()) {
                this.right = 0;
            } else {
                this.right = 2;
            }
        }
        return String.valueOf(c);
    }

    public boolean comp(String a, String b) {
        if (a.substring(b.length(), a.length()).equals(b)) {
            return true;
        }
        return false;
    }
}