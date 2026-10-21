cat > app.py <<'EOF'
def add(a, b):
    return a + b

if __name__ == "__main__":
    print("Jenkins CI Pipeline Demo")
    print("2 + 3 =", add(2, 3))
EOF