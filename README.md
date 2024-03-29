# YaBACOrganizer
This tool helps with editing BAC files for Xenoverse 2, which are responsible for various actions in a moveset and skill, such as animations, hitboxes, effects, sound, and more. 

This is not a guide on what each entry means.  This is just a tool to make editing them easier.  For a more comprehensive guide to that, please refer to the [Skill/Moveset Editing Manual](https://docs.google.com/document/d/18gaAbNCeJyTgizz5IvvXzjWcH9K5Q1wvUHTeWnp8M-E/edit#heading=h.v77lp7pp65pd)

Features include:
* Copying/Pasting/Adding/Deleting entries
* Smart pasting for items like EAN Indexes that are not the same between two movesets/skills
* Find/Replace entries by value
* Shared clipboard between different instances of the BAC organizer
* Convert Skills for use with the XV2 Skill Creator by Eternity easily

# Credits
* Eternity - Genser source code helped with the nitty gritty technical bits of the BAC file structure.
* Smithers,LazyBones, & Jackal - For the Skill/Moveset guide and the research into what each BAC entry field does.
* SK for the BAC Moveset Info file

# Changelog
```
0.1.0 - Initial Release
0.1.1 - Fixed bug saving after changing Projectile data, Fixed bug loading Transparency data.  
Fixed bug with Smart Paste not showing enough changes sometimes.
0.1.2 - Fixed floating point entries not being able to go negative
0.1.3 - Fixed bug on certain BAC files where when they don't have a BAC Entry 0, would not be able to read the file.
0.1.4 - Fixed visual bug with deleting BAC entries
0.1.5 - Fixed paste being broken.
0.1.6 - Fixed Part Invisibility not working
0.1.7 - Fixed deleting the wrong entries, fixed pasting entries with projectiles, fixed error when changing entry flags
0.1.8 - Added ability to drag/associate files to exe to open them, fixed Projectiles panel
0.1.9 - Fixed convert to skill editor
0.2.0 - Added support for BACType26
0.2.1 - Fixed bug with pasting, swapped x and y rotation in camera entry, fixed skill type in projectile panel
0.2.2 - Fixed floats not updating sometimes, fixed dummy BAC entries when saving, fixed throws on older BACs
0.2.3 - Fixed Throws loading incorrectly, fixed Type22 entries being unable to load
0.3.0 - * Changed backend TreeListCtrl
        * Added color picker for transparencies
        * Added floating point values for HomingMovement
        * Added more known values to various BACTypes
        * Changed a few controls where there may be lots of unknown values
        * Fixed Type22 not loading and saving properly
0.3.1 - Fixed append/inserts 
0.3.2 - Fixed paste/replace
0.3.3 - Add automatic backup creation on saving
0.3.4 - Fixed paste/replace
0.3.5 - Added BACType27, Fixed HomingMovement, renamed BACType18 to Physics and BACType26 to Extended Camera Control
0.3.6 - Updated Transform Control, BCMCallback, Projectile, and Acceleration with new Types/Flags
0.3.7 - Fixed BACType27 entries, swapped back x and y rotation for Camera
0.3.8 - Fixed issues with copying entries
0.3.9 - Fixed find/replace dialogs so it works with int/hex/float
0.4.0 - Merged Unleashed Edits 2.1 with main repo
```

