# ▶️ Execution Order

The generators should be executed in the following order.

---

# Step 1 — Master Data

```text
generate_machine_layout
        │
        ▼
generate_product_master
        │
        ▼
generate_tool_master
        │
        ▼
generate_operator_master
        │
        ▼
generate_operation_master
        │
        ▼
generate_press_program_master
        │
        ▼
generate_test_program_master
```

Commands:

```bash
python -m generator.master_data.generate_machine_layout

python -m generator.master_data.generate_product_master

python -m generator.master_data.generate_tool_master

python -m generator.master_data.generate_operator_master

python -m generator.master_data.generate_operation_master

python -m generator.master_data.generate_press_program_master

python -m generator.master_data.generate_test_program_master
```

---

# Step 2 — Manufacturing Simulation

```text
simulate_work_orders
        │
        ▼
generate_production_executions
        │
        ▼
simulate_operator_login
        │
        ▼
simulate_material_scan
        │
        ▼
generate_serial_numbers
        │
        ▼
simulate_press_operations
        │
        ▼
simulate_force_curves
        │
        ▼
simulate_testing
        │
        ▼
simulate_packaging
```

Commands:

```bash
python -m generator.simulation.simulate_work_orders

python -m generator.simulation.generate_production_executions

python -m generator.simulation.simulate_operator_login

python -m generator.simulation.simulate_material_scan

python -m generator.simulation.generate_serial_numbers

python -m generator.simulation.simulate_press_operations

python -m generator.simulation.simulate_force_curves

python -m generator.simulation.simulate_testing

python -m generator.simulation.simulate_packaging
```

---

# Output

After successful execution:

```
data/
├── master_data/
└── transactional_data/
```

will contain the complete synthetic manufacturing dataset.

---

# Notes

- Run all commands from the project root directory.
- Ensure the virtual environment is activated.
- Execute scripts in the documented order because later modules depend on previously generated datasets.