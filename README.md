# DWAK2 - An improved version of DWAK CPU architecture

DWAK2 is 64 bit. Therefore, all instructions are 64bit, and one word is 64bits.
Due to the simulation software limitations, addresses will be 24bit.


## TERMINOLOGY
- reg - means a register index.
    Can be one of: `R0`, `R1`, `R2`, `R3`, `CF`, `DV`, `SB`, `SH`, `IP`

- [mem] - means a memory address.
    Can be one of: `[const]`, `[reg]`

- const - means a constant value.
    Can be any hex, decimal, or binary number.


## REGISTERS
### General usage registers R0, R1, R2, R3.
Used in general computations.

- R0 has register index TODO, size of 64bits.
- R1 has register index TODO, size of 64bits.
- R2 has register index TODO, size of 64bits.
- R3 has register index TODO size of 64bits.

### Conditional flag register CF.
Contains a value that indicates the result of the last CMP instruction.

        0 means "equal", 1 means "not equal",
        2 means "less", 3 means "less equal",
        4 means "greater", 5 means "greater equal".
        
- CF has register index TODO, size of 3bits.

### Integer division register DV.
Used in DIVQ instruction to store the quotient and in DIVR instruction to store the remainder
    
- DV has register index TODO, size of 64bits.

### Stack registers SB, SH.
Used in stack operations. SB points to the base of the stack, and SH points to the head of the stack. 
    
- SB has register index TODO, size of 64bits.
- SH has register index TODO, size of 64bits.
    
### Instruction pointer register IP.
This is a special register that shoudn't be directly changed.
Points to the next instruction that has to be executed. 

- IP has register index 0xFF, size of 64bits.
----
#### Implementation
Registers are combined into one single regfile. 
It can both read two registers and write to one register.


## INSTRUCTIONS
### 1. MOV
Moves data from one location to another.
Can move data to registers or memory.
Can move data from registers, memory, or move constant values. However, can't move data from memory to memory.

#### Syntax:
```
MOV reg, reg        (opcode TODO)
MOV reg, [mem]      (opcode TODO)
MOV reg, const      (opcode TODO)
MOV [mem], reg      (opcode TODO)
MOV [mem], const    (opcode TODO)
```
#### Binary representation

```
MOV reg, reg
    3       =1. size in words
    8       =TODO. opcode
    8       register index (first argument)
    8       register index (second argument)
    37      unused
MOV reg, mem
    3       =1. size in words
    8       opcode TODO
    8-15    register index (first argument)
    16-39   memory address (second argument)
MOV reg, const
    0-7     opcode TODO
    8-15    register index (first argument)
    16-63   unused

    0-63    constant (second argument)
MOV mem, reg
    0-7     opcode TODO
    8-31    memory address (first argument)
    32-39   register index (second argument)
MOV mem, const
    0-7     opcode TODO
    8-31    memory address (first argument)
    32-63   unused
    
    0-63    constant (second argument)
```

## MEMORY:
### 1. Instruction memory - 8 words.
Contains instruction and data that has to be executed. Filled in fetch part of the cycle.

#### Implementation
It is a chip with three input pins that are used to write a word. 8 output pins are used to read words.
    
### 2. Program ROM - 2^10 words.
Contains the initial program. When DWAK starts, the program gets loaded into RAM at address 0.

#### implementation    
Implemented as an EEPROM and a circuit that loads itself into RAM when the computer boots.

The circuit simply reads 1024 words and writes them into RAM at the respectifull address. When it reaches 1024-th word, it toggles a register that stops further writing to RAM.

### 3. RAM - 2^24 words.
Random Access Memory. The initial program is loaded at address 0.       
Memory at the end of RAM is used for external devices. TODO(like VGA memory)

#### implementation
Implemented as a RAM with one write and two read ports.
    

## WHAT HAPPENS WHEN DWAK BOOTS:
The initial program in the ROM gets loaded into RAM at address 0. It starts executing the instructions


## WHAT HAPPENS AFTER DWAK BOOTS:
CPU performs a CPU cycle.
This happens in two stages.

### 1. Fetch
CPU reads the next instruction. It loads it, as well as its data (if opcode requires), into the instruction memory. 
Each word is read in one CPU cycle.
At the end of the Fetch stage, IP points to the next instruction.

### 2. Execute
CPU reads the content of the instruction memory, and sends its content to the right instruction chip. 
The chip then executes the instruction in one CPU cycle. 
All instruction chips have access to registers and RAM.

---
#### Implementation
There is a special thing called mode. There are 3 modes:
```
0 - read next instuction
1 - read and transfer data from RAM to the instruction memory
2 - execute instruction from the instruction memory
```


## HOW INSTRUCTION CHIPS WORK:
Each chip is given its input data that came from the instruction. 
If chip has to read some data from registers or RAM, it does it by sending the request to the output pins, which instantly deliver the request. 
Registers and RAM return the requested information instantly. The chip receives it. If now it has to read some more info - the process repeats.
When the chip is done reading, it instantly calculates the result data and sends it to registers and RAM to store.
Data is stored at the next CPU cycle.


## TODO
- [x] Design registers
- [x] Implements registers
- [x] Design RAM
- [x] Implement RAM
- [x] Design program ROM
- [x] Implement program ROM
- [x] Design instruction memory
- [x] Implement instruction memory 
- [x] Design Fetch stage
- [ ] Implement Fetch stage
- [x] Design `MOV`
- [ ] Implement `MOV`
- [ ] Design `ADD`
- [ ] Implement `ADD`
- [ ] Design `SUB`
- [ ] Implement `SUB`
- [ ] Design `MUL`
- [ ] Implement `MUL`
- [ ] Design `DIVQ`
- [ ] Implement `DIVQ`
- [ ] Design `DIVR`
- [ ] Implement `DIVR`
- [ ] Design `OR`
- [ ] Implement `OR`
- [ ] Design `AND`
- [ ] Implement `AND`
- [ ] Design `XOR`
- [ ] Implement `XOR`
- [ ] Design `NOT`
- [ ] Implement `NOT`
- [ ] Design `SHL`
- [ ] Implement `SHL`
- [ ] Design `SHR`
- [ ] Implement `SHR`
- [ ] Design `CMP`
- [ ] Implement `CMP`
- [ ] Design `JMP`
- [ ] Implement `JMP`
- [ ] Design `JE`
- [ ] Implement `JE`
- [ ] Design `JNE`
- [ ] Implement `JNE`
- [ ] Design `JL`
- [ ] Implement `JL`
- [ ] Design `JLT`
- [ ] Implement `JLT`
- [ ] Design `JG`
- [ ] Implement `JG`
- [ ] Design `JGT`
- [ ] Implement `JGT`
- [ ] Design `PUSH`
- [ ] Implement `PUSH`
- [ ] Design `POP`
- [ ] Implement `POP`
- [ ] Design `CALL`
- [ ] Implement `CALL`
- [ ] Design `RET`
- [ ] Implement `RET`

       
    
        
        
        
        

            
               
            
            
            
                
    
    
    
     



