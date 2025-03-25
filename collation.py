
root = tk.Tk()
root.title('Collation Master')
root.geometry('500x500')

style=ttk.Style(root)
root.tk.call("source", "forest-dark.tcl")
style.theme_use('forest-dark')

frame = tk.Frame(root)
frame.pack()

descriptionframe = ttk.LabelFrame(frame, text= 'Description')
descriptionframe.grid(row=0, column=0)


name_entry = ttk.Entry(descriptionframe)
name_entry.insert(0, "Name")
name_entry.grid(row=0, column=0, sticky='ew', pady=10, padx= 5)

full_length = ttk.Entry(descriptionframe)
full_length.insert(0, "Full Length")
full_length.bind("<FocusIn>", lambda  e:full_length.delete('0', 'end'))
full_length.grid(row=1, column= 0, sticky= 'ew', pady=10, padx=5)

double_length = ttk.Entry(descriptionframe)
double_length.insert(0, "Double Length")
double_length.bind("<FocusIn>", lambda  e:double_length.delete('0', 'end'))
double_length.grid(row=2, column= 0, sticky= 'ew', pady=10, padx=5)

add_data = ttk.Button(descriptionframe, text= 'Add Data', command=add_data)
add_data.grid(row=0, column= 1, sticky= 'ew', pady=10, padx=5)

power_cable = ttk.Entry(descriptionframe)
power_cable.insert(0, "Power Cable")
power_cable.bind("<FocusIn>", lambda  e:power_cable.delete('0', 'end'))
power_cable.grid(row=3, column= 0, sticky= 'ew', pady=10, padx=5)

drum_no = ttk.Entry(descriptionframe)
drum_no.insert(0, 'Drum No')
drum_no.bind('<FocusIn>', lambda e: drum_no.delete('0', 'end'))
drum_no.grid(row=4, column=0, sticky= 'ew', padx=5, pady=10)

length_mtrs = ttk.Entry(descriptionframe)
length_mtrs.insert(0, "Double Length")
length_mtrs.bind("<FocusIn>", lambda e:length_mtrs.delete('0', 'end'))
length_mtrs.grid(row=5, column= 0, sticky='ew', pady=10, padx=5)


update_button = ttk.Button(descriptionframe, text= 'Update', command= update)
update_button.grid(row= 1, column=1, sticky='ew', pady=10, padx=5 )


delete_button = ttk.Button(descriptionframe, text='Delete', command=delete)
delete_button.grid(row=2, column=1, sticky='ew', pady=10, padx=5)

save_button = ttk.Button(descriptionframe, text= 'Save', command=save)
save_button.grid(row=3, column=1, sticky='ew', padx=5, pady=10)

treeframe = ttk.Frame(frame)
treeframe.grid(row=0, column=1)

treescroll =ttk.Scrollbar(treeframe, orient='vertical')
treescroll.pack(side='right', fill='y')

cols = ('Name', 'Full length', 'Double length', 'Sum', 'Power Cable', 'Drum No', 'Length')
treeview = ttk.Treeview(treeframe, show= 'headings', columns= cols, height=13, yscrollcommand= treescroll.set)
treeview.column('Name', width = 200)
treeview.column('Full length', width = 100)
treeview.column('Double length', width = 100)
treeview.column('Sum', width = 100)
treeview.column('Power Cable', width = 200)
treeview.column('Drum No', width = 100)
treeview.column('Length', width = 100)

for col_name in cols:
    treeview.heading(col_name, text=col_name)
treescroll.config(command=treeview.yview)
treeview.pack()


root.mainloop()
