# python-ecommerce-pipeline-explore
A simple Python-based order management system using Object-Oriented Programming (OOP). This project demonstrates encapsulation, data processing, and basic financial calculations such as total revenue and tax computation

## Overview
This project is a simple Python-based order management system that demonstrates the use of Object-Oriented Programming (OOP), specifically **Encapsulation**.
The system allows users to:
- Create customer orders
- Store multiple orders
- Display order details
- Calculate total revenue
- Calculate total tax automatically

## Concept Used
## Encapsulation
Encapsulation is implemented by wrapping data and related methods inside classes:
- `Order` class → represents a single customer order
- `OrderProcessor` class → manages multiple orders
Each object stores its own data (order ID, customer name, date, and total amount) and provides methods to process that data.

## Features
- Add multiple orders
- Store orders in a list
- Display all orders
- Calculate total revenue
- Calculate total tax using a specified tax rate

## Testing / Simulation
I tested this program by:
- Adding **2–3 sample orders**
- Total revenue input example: **Rp 130,000**
- The program successfully calculated **10% tax = Rp 13,000 automatically**

This shows the system works correctly in handling data and performing calculations.

## How to Run
1. Make sure Python is installed
2. Run the file using:

```bash
python order.py
```

## Example Output
====== DAFTAR ORDER ======

                Order ID: A11
                Nama: Yusuf
                Tanggal: 2026-06-25
                Total: Rp. 30000
            
--------------------------------------------------

                Order ID: A12
                Nama: Abdulloh
                Tanggal: 2026-06-25
                Total: Rp. 100000
            
--------------------------------------------------
Total Pendapatan: Rp. 130000
Total Pajak: Rp. 13000.0

# Project Structure

.
├── order.py
└── README.md


## Future Improvements
- Add user input (CLI)
- Search order by ID
- Update and delete order
- Export data to CSV/Excel
- Add database integration


## Author
- Yusuf Abdulloh
