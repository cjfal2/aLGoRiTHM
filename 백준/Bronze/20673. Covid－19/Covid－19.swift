if let a = Int(readLine() ?? ""), let b = Int(readLine() ?? "") {
    if a <= 50 && b <= 10 {
        print("White")
    } else if b > 30 {
        print("Red")
    } else {
        print("Yellow")
    }
}
