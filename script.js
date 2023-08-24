// Import the functions you need from the SDKs you need
import { initializeApp } from 'firebase/app';
import { getAuth } from 'firebase/auth';
import { getFirestore } from 'firebase/firestore';

// Your web app's Firebase configuration
const firebaseConfig = {
  apiKey: 'AIzaSyBfD0A3fKBFNt8XgIaLxnQo199pEbpsUPE',
  authDomain: 'trim-axle-340015.firebaseapp.com',
  projectId: 'trim-axle-340015',
  storageBucket: 'trim-axle-340015.appspot.com',
  messagingSenderId: '1086751176937',
  appId: '1:1086751176937:web:f9d5401f16e891d5079878',
  measurementId: 'G-DV23584DS7'
};

// Initialize Firebase
const app = initializeApp(firebaseConfig);
const auth = getAuth(app);
const firestore = getFirestore(app);

// You can use the following code to sign in a user with Google:
import { signInWithPopup, GoogleAuthProvider } from 'firebase/auth';
const provider = new GoogleAuthProvider();
signInWithPopup(auth, provider)
  .then((result) => {
    // ...
  }).catch((error) => {
    // ...
  });

// You can use the following code to get the currently signed-in user:
import { onAuthStateChanged } from 'firebase/auth';
onAuthStateChanged(auth, (user) => {
  if (user) {
    // User is signed in
    const uid = user.uid;
    // ...
  } else {
    // User is signed out
    // ...
  }
});