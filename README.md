# Athena Challenge

Application will have the form

```json
{
    "mortgage":{
       "income": 0.00,
       "expense": 1234.45,
       "frequency": 1 
    },
    "random expense": {
        "income": 0,
        "expense": 4000,
        "frequency": 1
    }       
}
```

There will be an entry per cashflow, and each entry will contain three fields `income`, `expense` & `frequency`


* `income` relates to an in flowing cash flow
* `expense` relates to an out flowing cash flow
* `frequency` relates to the number of that cash flow **per month**