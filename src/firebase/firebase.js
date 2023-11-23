import { initializeApp } from "firebase/app";
import { getFirestore } from "firebase/firestore";

const firebaseConfig = {
  apiKey: "AIzaSyAxyuiS09RQncms4_vMg01hBU-LctpB7tY",
  authDomain: "thanawin-iccs340.firebaseapp.com",
  projectId: "thanawin-iccs340",
  storageBucket: "thanawin-iccs340.appspot.com",
  messagingSenderId: "405640940173",
  appId: "1:405640940173:web:72c351ca621048ccf6f0c4",
};

// Initialize Firebase
const app = initializeApp(firebaseConfig);
const db = getFirestore(app);

export { db };
