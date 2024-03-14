---
id: luzjmeysann3hc8qzv037y1
title: Neural Network
desc: ""
updated: 1704146487115
created: 1704146273568
---

- [Wikipedia page](https://en.wikipedia.org/wiki/Artificial_neural_network)

## Python code snippet

The Python code snippet provides an overview of the training function, which uses the training dataset, number of hidden layer units, learning rate, and number of iterations as parameters:

```python
def train(X, y, n_hidden, learning_rate, n_iter):
    m, n_input = X.shape

    # 1. random initialize weights and biases
    w1 = np.random.randn(n_input, n_hidden)
    b1 = np.zeros((1, n_hidden))
    w2 = np.random.randn(n_hidden, 1)
    b2 = np.zeros((1, 1))

    # 2. in each iteration, feed all layers with the latest weights and biases
    for i in range(n_iter + 1):
        z2 = np.dot(X, w1) + b1
        a2 = sigmoid(z2)
        z3 = np.dot(a2, w2) + b2
        a3 = z3
        dz3 = a3 - y
        dw2 = np.dot(a2.T, dz3)
        db2 = np.sum(dz3, axis=0, keepdims=True)
        dz2 = np.dot(dz3, w2.T) * sigmoid_derivative(z2)
        dw1 = np.dot(X.T, dz2)
        db1 = np.sum(dz2, axis=0)

        # 3. update weights and biases with gradients
        w1 -= learning_rate * dw1 / m
        w2 -= learning_rate * dw2 / m
        b1 -= learning_rate * db1 / m
        b2 -= learning_rate * db2 / m

        if i % 1000 == 0:
            print("Epoch", i, "loss: ", np.mean(np.square(dz3)))

    model = {"w1": w1, "b1": b1, "w2": w2, "b2": b2}
    return model
```
