---
author: gbmhunter
date: 2013-05-31 00:42:25+00:00
draft: false
title: Detecting Key Presses
type: page
url: /programming/languages/c-sharp/detecting-key-presses
---

# WinForms

Use the following code to detect a key press when focus is on a particular object.

**Note: There is different syntax for WPF.**

```c#    
TextBox tb = new TextBox();

// Assign a new event handler
tb.KeyDown += new KeyEventHandler(tb_KeyDown);

// The event handler
private void tb_KeyDown(object sender, KeyEventArgs e)
{
    if (e.KeyCode == Keys.Enter)
    {
            //Enter key is down

            //Capture the text
            if (sender is TextBox)
            {
                TextBox txb = (TextBox)sender;
                MessageBox.Show(txb.Text);
            }
    }
}
```

# WPF

## Non-Binding Method

Use the following code to detect a key press when focus is on a particular object.

**Note: There is different syntax for WinForms.**

```c#    
TextBox tb = new TextBox();

// Assign a new event handler
tb.KeyDown += new KeyEventHandler(tb_KeyDown);

private void tb_KeyDown(object sender, KeyEventArgs e)
{
    if (e.Key == Key.Enter)
    {
        e.Handled = true;
        MessageBox.Show("You pressed Enter!");
    }
}
```