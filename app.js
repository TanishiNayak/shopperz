const close = document.querySelector(".close");
const open = document.querySelector(".ham");
const menu = document.querySelector(".menu");
close.addEventListener("click", () => {
  menu.style.visibility = "hidden";
});
open.addEventListener("click", () => {
  menu.style.visibility = "visible";
});


// const productListElement = document.getElementById("productList");

// fetch("productdata.csv")
//     .then(response => response.text())
//     .then(csvData => {
//         const lines = csvData.split('\n');
//         const header = lines[0].split(',');

//         for (let i = 1; i < lines.length; i++) {
//             const values = lines[i].split(',');
//             if (values.length === header.length) {
//                 const product = {};
//                 for (let j = 0; j < header.length; j++) {
//                     product[header[j]] = values[j];
//                 }

//                 const productElement = document.createElement("div");
//                 productElement.classList.add("product");
//                 productElement.innerHTML = `
//                     <h2>${product["Product Name"]}</h2>
//                     <p>Price: $${product["Price"]}</p>
//                     <p>Category: ${product["Category"]}</p>
//                 `;

//                 productListElement.appendChild(productElement);
//             }
//         }
//     })
//     .catch(error => {
//         console.error("Error fetching data:", error);
//     });
