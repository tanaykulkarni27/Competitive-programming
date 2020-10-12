<center><h1>Pseudo Codes for Data Structures</h1></center><br>
<hr>
<h2> Linked List</h2><br>
<p><br>
Class Node {&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;// class creating Nodes for Linked List <br>
  int data;<br>
  Node node;<br>
  Node(data){<br>
  this.data = data<br>
  this.next = Null<br>
  }<br>
  void add(data){ &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;// function to link next node with the previous one <br>
  this.next = Node(data)<br>
  }<br>
  }<br>
</p><br>
class LinkedList{&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; // Main class implement Linked List  <br>
   LinkedList(){ <br>
       this.Node = None<br>
        this.previous = None<br>
        }<br><br>
    void add(data):<br>
        if this.previous == None{&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;// if we are creating the node for first time it creates a head Node<br>
           this.Node = Node(data)<br>
            this.previous = self.Node<br>
            }<br><br>
        else{&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;// if we already have any data add's the data to the previous Node<br>
            this.previous.next = Node(data)<br>
            thisprevious = self.previous.next<br>
            }<br>
            }<br>
<hr>
