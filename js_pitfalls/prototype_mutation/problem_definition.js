/***
 * 
 * Figure out the bug in the following implementation of prototype delegation
 * by writing tests that assert the contents of each foo instance
 * 
 */
/*
/* var fooProto = {
     isBaz: function isBaz() {
         return this.state;
     },

     bar: function bar() {
         this.state = !this.state;
         return this;
     },

     meta: {
         name: 'bim',
     },

     state: false
 };


 const foo1 = Object.create(fooProto);
 const foo2 = Object.create(fooProto);
 const foo3 = Object.create(fooProto);

foo1.meta.name = 'Bruce Lee';
foo1.bar();
foo2.meta.name = 'Samuel L. Jackson';
foo1.bar();
foo3.meta = {name: 'Big Bird'};
