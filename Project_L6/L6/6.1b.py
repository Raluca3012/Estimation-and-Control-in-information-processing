import matplotlib.pyplot as plt


original = "Buna dimineata! Bine ai venit! Bine ati venit! Bine ne-am gasit! Aspecte frumoase pentru un inceput de zi si de saptamana! Hai sa vedem."

texts = [
    "Buna dimineata Bine ai venit Bine ati venit Bine ne am gasit Aspecte frumoase pentru un inceput de zi si de saptamana Hai sa vedem",
    "Buna dimineata Bine ai venit Bine ati venit Bine ne am gasit Aspecte frumoase pentru inceput de zi si de saptamana Hai sa vedem",
    "Buna dimineata Bine ai venit Bine ati venit Bine ne am gasit Aspecte frumoase pentru zi si saptamana Hai vedem",
    "Buna dimineata Bine venit Bine ati venit Bine ne gasit Aspecte pentru zi saptamana vedem"
]

distances = [0.5, 0.7, 1, 2] 

def wer(reference, hypothesis):
    ref = reference.split()
    hyp = hypothesis.split()

    d = [[0]*(len(hyp)+1) for _ in range(len(ref)+1)]

    for i in range(len(ref)+1):
        d[i][0] = i
    for j in range(len(hyp)+1):
        d[0][j] = j

    for i in range(1, len(ref)+1):
        for j in range(1, len(hyp)+1):
            cost = 0 if ref[i-1] == hyp[j-1] else 1
            d[i][j] = min(
                d[i-1][j] + 1,
                d[i][j-1] + 1,
                d[i-1][j-1] + cost
            )

    return d[-1][-1] / len(ref)


errors = [wer(original, t) for t in texts]


for d, e in zip(distances, errors):
    print(f"Distance {d} m -> WER: {e:.2f}")

plt.plot(distances, errors, marker='o')
plt.xlabel("Distance (m)")
plt.ylabel("Word Error Rate")
plt.title("Speech Recognition Error vs Distance")
plt.grid()
plt.show()