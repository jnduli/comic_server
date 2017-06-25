##########
Comic Site
##########

This is a project that will manage a webcomic site. How it will
work is as follows:

1. The comic writer creates an account which
   has to be approved by the admin.
2. The admin approves / rejects the comic writer account.
3. The comic writer uploads a comic strip to the server.
4. The strip should be a series of images labelled 1,2,3.
5. Each strip should be the same size.
6. A short description and title should be added to the comic
7. The comic is given a unique identifier based on the writer name
   e.g. writer_1
8. The comic is uploaded as a draft and the writer is directed to
   a sample view that shows how it will look like for the end
   users.
9. Afterwards the writer can change the comic to published so that
   it can be published.
10. If the comic writer wants another writer's comment on the
    comic, s/he can request a review from the site.


Definitions
===========

+ Concept: This is a textual description of how the comic should
  look like. It contains a description of the characters, the
  conversations they have, sample name of the comic, etc.
+ Sketch: This is a sketch of the comic based off the concept. It
  is usually done on paper and an image uploaded for reference. A
  sketch can be independent or linked to a concept
+ Comic: This is the complete comic strip.


Permissions
===========

+ Concept:
  - can_add_concept
  - can_edit_concept
  - can_remove_concept
  - can_share_concept
+ Sketch:
  - can_add_sketch
  - can_remove_sketch
  - can_share_sketch
+ Comic:
  - can_add_comic
  - can_edit_comic
  - can_remove_comic
  - can_publish_comic

Roles Design
============


- Writer role:
  - can_add_concept
  - can_edit_concept
  - can_remove_concept
  - can_share_concept
  - can_add_sketch
  - can_remove_sketch
  - can_share_sketch
  - can_add_comic
  - can_edit_comic
  - can_remove_comic
  - can_publish_comic

- Admin_role:
     can_approve_writer
     can_depublish_comic
     can_review_comic


Dbase design
============
Concept:
    characters_no
    comic_strips_no
    conversation
    environment
    user_id
    deleted

Sketch:
    concept_id
    sketch_image
    user_id
    deleted

Comic:
    user_id
    sketch_id
    description
    slug
    published
    deleted

Comic_images:
    comic_id
    image
    positioning
