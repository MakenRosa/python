print("=" * 30)
print(f"{'10 TERMOS DE UMA PA':^30}")
print("=" * 30)

primeiro_termo = int(input("Primeiro termo: "))
razao = int(input("Razão: "))

for c in range(1, 11):
    print(f"{primeiro_termo} -> ", end="")
    primeiro_termo += razao

print("ACABOU")