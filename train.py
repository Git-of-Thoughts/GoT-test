import torch
from torch import nn, optim
from torch.utils.data import DataLoader
from torchvision import datasets, transforms
from autoencoder import Autoencoder

def train():
    transform = transforms.ToTensor()
    mnist = datasets.MNIST('.', download=True, transform=transform)
    dataloader = DataLoader(mnist, batch_size=64, shuffle=True)

    device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
    model = Autoencoder().to(device)
    criterion = nn.MSELoss()
    optimizer = optim.Adam(model.parameters())

    epochs = 10
    for epoch in range(epochs):
        for img, _ in dataloader:
            img = img.to(device)
            output = model(img)
            loss = criterion(output, img)

            optimizer.zero_grad()
            loss.backward()
            optimizer.step()

    torch.save(model.state_dict(), 'autoencoder.pth')
