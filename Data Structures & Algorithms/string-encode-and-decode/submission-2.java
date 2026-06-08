class Solution {
    String eof = "<EOF>";
    String empty = "<EMPTY>";

    public String encode(List<String> strs) {
        
        StringBuilder sb = new StringBuilder();
        if (strs.size() == 0) return null;
        
        
        for(String s:strs){
            if (s.equals("")){
                sb.append(empty);
            }else{
                sb.append(s);
            }
            
            sb.append(eof);
        }
        return sb.toString();

    }

    public List<String> decode(String str) {
        if (str == null) return new ArrayList<String>();
        String[] strs = str.split(eof);
        List<String> res = new ArrayList<>();
        for (String s:strs){
            if (!s.equals(eof)){
                if (s.equals(empty)){
                    res.add("");
                }else{
                    res.add(s);
                }
                
            }
        }
        return res;
    }
}
