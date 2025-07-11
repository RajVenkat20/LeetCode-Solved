class Solution:
    def reformatDate(self, date: str) -> str:
        months = {"Jan": "01", 
                  "Feb": "02", 
                  "Mar": "03", 
                  "Apr": "04", 
                  "May": "05", 
                  "Jun": "06", 
                  "Jul": "07", 
                  "Aug": "08", 
                  "Sep": "09", 
                  "Oct": "10", 
                  "Nov": "11", 
                  "Dec": "12"}
        
        dd, mm, yyyy = date.split()
        
        dd = dd[:-2]
        if(len(dd) == 1):
            dd = "0" + dd        
        mm = months[mm]

        return "-".join([yyyy, mm, dd])