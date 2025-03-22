class FirstRecurringNum:
    def first_recurring(self,arr):
        dict = {}
        for n in arr:
            if n in dict:
                return f"value -> {n} is first recurring"
            else:
                dict[n] = 1
        return "no recurring value"
        

if __name__ == "__main__":
    print("Hello from main")
    f = FirstRecurringNum()
    print(f.first_recurring([2,5,1,2,3,5,1,2,4]))
    print(f.first_recurring([2,1,1,2,3,5,1,2,4]))
    print(f.first_recurring([2,3,4,5]))