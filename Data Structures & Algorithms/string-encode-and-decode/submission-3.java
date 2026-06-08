class Solution {

    public String encode(List<String> strs) {
        StringBuilder sb = new StringBuilder();
        
        for (String s:strs){
            int length = 0;
            StringBuilder tmp = new StringBuilder();
            for (int i = 0; i < s.length(); i++){
                length += 1;
                tmp.append(s.charAt(i));
            }
            sb.append(String.valueOf(length));
            sb.append("#");
            sb.append(tmp);
        }
        return sb.toString();
    }

    public List<String> decode(String str) {
        List<String> res = new ArrayList<String>();
        int i = 0;
        while (i < str.length()){
            StringBuilder cnt = new StringBuilder();
            while (Character.isDigit(str.charAt(i))){
                cnt.append(str.charAt(i));
                i+=1;
            }
            i += 1; // skip # 
            StringBuilder s = new StringBuilder();
            int length = Integer.parseInt(cnt.toString());
            for (int j = 0; j < length; j++){
                s.append(str.charAt(i));
                i += 1;
            }
            res.add(s.toString());
        }
        return res;
    }
}
