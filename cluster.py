import torch
from sklearn.cluster import KMeans
from autoencoder import Autoencoder, Encoder

def cluster():
    device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
    model = Autoencoder().to(device)
    model.load_state_dict(torch.load('autoencoder.pth'))
    model.eval()

    encoder = Encoder().to(device)
    encoder.load_state_dict(model.encoder.state_dict())

    mnist = datasets.MNIST('.', download=True, transform=transforms.ToTensor())
    dataloader = DataLoader(mnist, batch_size=len(mnist), shuffle=True)

    for img, _ in dataloader:
        img = img.to(device)
        latent = encoder(img).detach().cpu().numpy()

    kmeans = KMeans(n_clusters=10)
    kmeans.fit(latent)
