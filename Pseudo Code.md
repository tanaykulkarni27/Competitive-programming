<center><h1>Pseudo Codes for Data Structures</h1></center>
<h2> Linked List</h2>
<p>
Class Node {   // class creating Nodes for Linked List 
  int data;
  Node node;
  Node(data){
  this.data = data
  this.next = Null
  }
  void add(data){   // function to link next node with the previous one 
  this.next = Node(data)
  }
  }
</p>
